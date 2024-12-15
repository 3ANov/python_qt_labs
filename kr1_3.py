import sys
import math
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Инициализация интерфейса
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Вычисление выражения")

        # Создание элементов
        self.x_label = QLabel('Введите x:')
        self.result_label = QLabel('Результат: ')

        self.x_input = QLineEdit()

        self.calculate_button = QPushButton('Вычислить')
        self.calculate_button.clicked.connect(self.calculate)

        # Размещение элементов на форме
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.x_label)
        form_layout.addWidget(self.x_input)
        form_layout.addWidget(self.calculate_button)
        form_layout.addWidget(self.result_label)

        self.setLayout(form_layout)

    def calculate(self):
        try:
            # Получение значения x из поля ввода
            x = float(self.x_input.text())

            # Применение условий для вычисления y
            if x <= 0:
                y = math.exp(-x)  # y = exp(-x)
            elif 0 < x <= 1:
                y = math.cos(x * math.pi / 2)  # y = cos(x * pi / 2)
            else:
                y = 0  # y = 0, если x > 1

            # Отображение результата
            self.result_label.setText(f'Результат: {y}')
        except ValueError:
            self.result_label.setText('Ошибка ввода!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())

