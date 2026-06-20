from PySide6.QtWidgets import QApplication,QMainWindow
import sys

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self,title="My To-do App"):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(600,400)


window = MainWindow()
window.show()

sys.exit(app.exec())