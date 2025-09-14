from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

def show_input():
    text = input_box.text()

app = QApplication([])

window = QWidget()
window.setWindowTitle("Azurite")
window.setGeometry(100, 100, 300, 100)

layout = QVBoxLayout()


input_box = QLineEdit()
input_box.setPlaceholderText("Enter your token.")
layout.addWidget(input_box)

button = QPushButton("Import")
button.clicked.connect(show_input)
layout.addWidget(button)

window.setLayout(layout)
window.show()

app.exec()
