import sys
import random
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QLineEdit

class MatrixCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Поиск максимальных элементов")

        # Создание элементов интерфейса
        self.size_label = QLabel("Введите размер матрицы (строки, столбцы):")
        self.size_input = QLineEdit(self)
        self.size_input.setPlaceholderText("например: 4,4")

        self.generate_button = QPushButton("Сгенерировать матрицу", self)
        self.find_button = QPushButton("Найти максимальные элементы", self)

        # Метка для вывода результата
        self.result_label = QLabel("Результат: ", self)

        # Создание таблицы для вывода матрицы
        self.table = QTableWidget(self)

        # Подключаем кнопки к функциям
        self.generate_button.clicked.connect(self.generate_matrix)
        self.find_button.clicked.connect(self.find_max_elements)

        # Размещение элементов на форме
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.size_input)
        input_layout.addWidget(self.generate_button)

        layout = QVBoxLayout()
        layout.addWidget(self.size_label)
        layout.addLayout(input_layout)
        layout.addWidget(self.table)
        layout.addWidget(self.find_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def generate_matrix(self):
        # Получаем размеры матрицы из ввода
        size_text = self.size_input.text()
        try:
            rows, cols = map(int, size_text.split(','))  # Разбиваем строку и конвертируем в int
            self.table.setRowCount(rows)
            self.table.setColumnCount(cols)

            # Заполняем таблицу случайными целыми числами от -10 до 10
            for row in range(rows):
                for col in range(cols):
                    random_value = random.randint(-10, 10)
                    self.table.setItem(row, col, QTableWidgetItem(str(random_value)))

            self.result_label.setText("Матрица сгенерирована. Нажмите 'Найти максимальные элементы'.")

        except ValueError:
            self.result_label.setText("Ошибка! Введите корректный размер матрицы.")

    def find_max_elements(self):
        # Инициализация переменных для максимального элемента
        max_row = max_col = -1  # Строка и столбец для максимального элемента
        max_value = None  # Для первого элемента будет присвоено значение сразу

        # Проходим по всем ячейкам таблицы, чтобы найти максимальный элемент
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                value = int(item.text())  # Преобразуем значение в целое число

                if max_value is None:  # Присваиваем первое значение
                    max_value = value
                    max_row, max_col = row, col
                elif abs(value) > abs(max_value):  # Сравниваем по абсолютной величине
                    max_value = value
                    max_row, max_col = row, col  # Обновляем строку и столбец для максимального элемента

        # Выводим результат
        if max_row != -1 and max_col != -1:
            self.result_label.setText(f"Максимальный элемент по абс. значению: {max_value} на позиции: ({max_row+1}, {max_col+1})")
        else:
            self.result_label.setText("Матрица пуста или содержит неверные данные.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MatrixCalculator()
    window.show()
    sys.exit(app.exec())
