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
        self.x_label = QLabel('x:')
        self.y_label = QLabel('y:')
        self.a_label = QLabel('a:')
        self.b_label = QLabel('b:')
        self.result_label = QLabel('Результат: ')

        self.x_input = QLineEdit()
        self.y_input = QLineEdit()
        self.a_input = QLineEdit()
        self.b_input = QLineEdit()

        self.calculate_button = QPushButton('Вычислить')
        self.calculate_button.clicked.connect(self.calculate)

        # Размещение элементов на форме
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.x_label)
        form_layout.addWidget(self.x_input)
        form_layout.addWidget(self.y_label)
        form_layout.addWidget(self.y_input)
        form_layout.addWidget(self.a_label)
        form_layout.addWidget(self.a_input)
        form_layout.addWidget(self.b_label)
        form_layout.addWidget(self.b_input)
        form_layout.addWidget(self.calculate_button)
        form_layout.addWidget(self.result_label)

        self.setLayout(form_layout)

    def calculate(self):
        try:
            # Получение значений из полей ввода
            x = float(self.x_input.text())
            y = float(self.y_input.text())
            a = float(self.a_input.text())
            b = float(self.b_input.text())

            # Вычисление числителя
            tg_part = math.tan(a * (x / y))  # tg(a * (x / y))
            ctg_part = 1 / math.tan(b * (y / a))  # ctg(b * (y / a))
            numerator = tg_part - ctg_part

            # Вычисление знаменателя
            denominator = a * (x**2) + b * (y**2)

            # Вычисление дроби
            fraction = numerator / denominator

            # Вычисление экспоненты
            exp_part = math.exp(math.sqrt(a * x) + math.sqrt(b * y))

            # Итоговое значение
            F = fraction * exp_part

            # Отображение результата
            self.result_label.setText(f'Результат: {F}')
        except ValueError:
            self.result_label.setText('Ошибка ввода!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())

