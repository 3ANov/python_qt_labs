import math
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class SumCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Вычисление суммы")

        # Создание элементов интерфейса
        self.result_label = QLabel("Результат:")

        self.calculate_button = QPushButton('Вычислить')
        self.calculate_button.clicked.connect(self.calculate)

        # Размещение элементов на форме
        layout = QVBoxLayout()
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate(self):
        try:
            # Установим x = 1
            x = 1

            # Инициализация суммы
            s = math.exp(x)

            # Вычисление суммы по формуле для i от 2 до 10
            for i in range(2, 11):
                s += 1 / math.factorial(i)

            # Выводим результат
            self.result_label.setText(f"Сумма: {s:.6f}")

        except ValueError:
            self.result_label.setText("Ошибка вычислений.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SumCalculator()
    window.show()
    sys.exit(app.exec())
