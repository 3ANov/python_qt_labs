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
            n = 10
            s = sum((math.exp(x) + i) / math.factorial(i + 1) for i in range(2, n + 1))

            # Выводим результат
            self.result_label.setText(f"Сумма: {s:.6f}")

        except ValueError:
            self.result_label.setText("Ошибка вычислений.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SumCalculator()
    window.show()
    sys.exit(app.exec())
