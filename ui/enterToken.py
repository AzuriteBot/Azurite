from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton

def enterToken():
    class TokenDialog(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Azurite")
            self.setGeometry(100, 100, 300, 100)
            self.token = None

            layout = QVBoxLayout()
            self.input_box = QLineEdit()
            self.input_box.setPlaceholderText("Enter your token.")
            layout.addWidget(self.input_box)

            button = QPushButton("Import")
            button.clicked.connect(self.accept)
            layout.addWidget(button)

            self.setLayout(layout)

        def accept(self):
            self.token = self.input_box.text()
            super().accept()

    app = QApplication([])
    dialog = TokenDialog()
    dialog.exec()  # block tới khi user click Import
    return dialog.token
