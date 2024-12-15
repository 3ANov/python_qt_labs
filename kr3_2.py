import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QHBoxLayout, QLineEdit

class SequenceCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Фильтрация последовательности")

        # Создание элементов интерфейса
        self.input_label = QLabel("Введите элемент и нажмите 'Добавить':")

        # Список для добавления элементов
        self.input_field = QLineEdit()

        # Кнопки для управления
        self.add_button = QPushButton("Добавить")
        self.calculate_button = QPushButton("Вычислить")

        # Списки для отображения элементов
        self.input_list = QListWidget()
        self.result_list = QListWidget()

        # Подключаем кнопки к функциям
        self.add_button.clicked.connect(self.add_element)
        self.calculate_button.clicked.connect(self.calculate)

        # Создание лейаута для ввода
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.add_button)

        # Размещение элементов на форме
        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addLayout(input_layout)
        layout.addWidget(self.input_list)
        layout.addWidget(self.calculate_button)
        layout.addWidget(QLabel("Отфильтрованные элементы:"))
        layout.addWidget(self.result_list)

        self.setLayout(layout)

    def add_element(self):
        # Получаем введенный элемент и добавляем его в input_list
        text = self.input_field.text()
        if text:
            self.input_list.addItem(text)
            self.input_field.clear()

    def calculate(self):
        try:
            # Получаем все элементы из input_list
            x = []
            for i in range(self.input_list.count()):
                x.append(int(self.input_list.item(i).text()))  # Преобразуем строку в целое число

            # Создание новой последовательности y без нулевых элементов
            y = [elem for elem in x if elem != 0]

            # Очищаем result_list и добавляем элементы в result_list
            self.result_list.clear()
            for elem in y:
                self.result_list.addItem(str(elem))

            # Выводим количество оставшихся элементов
            self.result_list.addItem(f"Оставшиеся элементы: {len(y)}")

        except ValueError:
            self.result_list.addItem("Ошибка ввода! Пожалуйста, введите только числа.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SequenceCalculator()
    window.show()
    sys.exit(app.exec_())
