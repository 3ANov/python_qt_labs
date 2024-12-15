import sys
import math
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class FunctionCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Вычисление функции на промежутке")

        # Создание элементов интерфейса
        self.a_label = QLabel("Введите значение a:")
        self.b_label = QLabel("Введите значение b:")
        self.h_label = QLabel("Введите шаг h:")

        self.a_input = QLineEdit()
        self.b_input = QLineEdit()
        self.h_input = QLineEdit()

        self.result_label = QLabel("Результат:")

        self.calculate_button = QPushButton('Вычислить')
        self.calculate_button.clicked.connect(self.calculate)

        # Размещение элементов на форме
        layout = QVBoxLayout()
        layout.addWidget(self.a_label)
        layout.addWidget(self.a_input)
        layout.addWidget(self.b_label)
        layout.addWidget(self.b_input)
        layout.addWidget(self.h_label)
        layout.addWidget(self.h_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate(self):
        try:
            # Получаем значения a, b и h
            a = float(self.a_input.text())
            b = float(self.b_input.text())
            h = float(self.h_input.text())

            # Начальный x
            x = a
            results = []

            # Цикл с предусловием (while)
            while x <= b:
                if x < -math.pi:
                    y = math.pi - (x + math.pi) ** 2
                elif -math.pi <= x <= math.pi:
                    y = math.pi + math.cos(x) + 1
                else:
                    y = math.pi + (x - math.pi) ** 2

                results.append(f"x = {x:.2f}, y = {y:.2f}")
                x += h  # Переход к следующему значению x

            # Выводим результаты
            self.result_label.setText("\n".join(results))
        except ValueError:
            self.result_label.setText("Ошибка ввода! Пожалуйста, введите числовые значения.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FunctionCalculator()
    window.show()
    sys.exit(app.exec())

