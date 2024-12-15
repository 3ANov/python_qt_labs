import sys
import math
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

# Функция для генерации диапазона чисел с шагом для вещественных чисел
def frange(start, stop, step):
    while start <= stop:
        yield round(start, 6)  # Округляем до 6 знаков после запятой
        start += step

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

            # Генерация значений x с шагом h
            results = []
            for x in frange(a, b, h):
                if x < -3:
                    y = 7 * math.sqrt(abs(x - 1)) - 11
                elif -3 <= x <= 3:
                    y = x
                else:
                    y = 7 * math.sqrt(x + 1) - 11

                results.append(f"x = {x:.2f}, y = {y:.2f}")

            # Выводим результаты
            self.result_label.setText("\n".join(results))
        except ValueError:
            self.result_label.setText("Ошибка ввода! Пожалуйста, введите числовые значения.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FunctionCalculator()
    window.show()
    sys.exit(app.exec())

