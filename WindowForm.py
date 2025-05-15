import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Мое первое PyQt5 приложение")
        self.setMinimumSize(400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.label = QLabel("Введите ваше имя:")
        self.text_input = QLineEdit()
        input_layout.addWidget(self.label)
        input_layout.addWidget(self.text_input)
        main_layout.addLayout(input_layout)

        button_layout = QHBoxLayout()
        self.button = QPushButton("Поздороваться")
        self.button.clicked.connect(self.say_hello)
        button_layout.addStretch()
        button_layout.addWidget(self.button)
        main_layout.addLayout(button_layout)

        central_widget.setLayout(main_layout)

    def say_hello(self):
        name = self.text_input.text()
        self.label.setText(f"Привет, {name}!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())