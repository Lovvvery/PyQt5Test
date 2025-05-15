import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Обработка данных в PyQt5")
        self.setMinimumSize(400, 200)
        self.user_name = ""

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
        self.save_button = QPushButton("Сохранить имя")
        self.save_button.clicked.connect(self.save_name)

        self.load_button = QPushButton("Загрузить имя")
        self.load_button.clicked.connect(self.load_name)

        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.load_button)
        main_layout.addLayout(button_layout)


        self.greeting_label = QLabel("")
        main_layout.addWidget(self.greeting_label)

        central_widget.setLayout(main_layout)


    def save_name(self):
        self.user_name = self.text_input.text().strip()

        if self.user_name:
            try:
                with open("username.txt", "w", encoding="utf-8") as file:
                    file.write(self.user_name)
                self.greeting_label.setText(f"Привет, {self.user_name}!")
            except Exception as e:
                self.show_error(f"Ошибка при сохранении: {e}")
        else:
            self.show_error("Имя не может быть пустым!")


    def load_name(self):
        if os.path.exists("username.txt"):
            try:
                with open("username.txt", "r", encoding="utf-8") as file:
                    self.user_name = file.read().strip()
                self.text_input.setText(self.user_name)
                self.greeting_label.setText(f"Добро пожаловать снова, {self.user_name}!")
            except Exception as e:
                self.show_error(f"Ошибка при чтении файла: {e}")
        else:
            self.show_error("Файл с именем не найден.")


    def show_error(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Ошибка")
        msg_box.setText(message)
        msg_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())