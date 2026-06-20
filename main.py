from PySide6.QtWidgets import QApplication,QMainWindow,QVBoxLayout,QWidget,QPushButton,QHBoxLayout,QLineEdit,QListWidget,QListWidgetItem
import sys

from PySide6.QtCore import Qt

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self,title="My To-do App"):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(600,400)


        outer = QVBoxLayout()
        inner = QHBoxLayout()

        # add button and input
        addBtn = QPushButton("Add")
        addBtn.clicked.connect(self.add_task)

        deleteBtn = QPushButton("delete")
        deleteBtn.clicked.connect(self.delete_task)

        self.inputLine = QLineEdit(placeholderText="Enter the task")
        self.inputLine.returnPressed.connect(self.add_task)

        inner.addWidget(addBtn)
        inner.addWidget(self.inputLine)
        inner.addWidget(deleteBtn)

        outer.addLayout(inner)


        self.list_widget = QListWidget()
        self.list_widget.itemChanged.connect(self.item_toggled)
        outer.addWidget(self.list_widget)


        container = QWidget()
        container.setLayout(outer)

        self.setCentralWidget(container)
    
    def add_task(self):
        task = self.inputLine.text()

        if task != "":
            task_widget = QListWidgetItem(task)
            task_widget.setFlags(task_widget.flags() | Qt.ItemIsUserCheckable)
            task_widget.setCheckState(Qt.Unchecked)

            self.list_widget.addItem(task_widget)
            self.inputLine.clear()

    def delete_task(self):
        # print("Delete...")
        row = self.list_widget.currentRow()

        if row != -1:
            self.list_widget.takeItem(row)

    def item_toggled(self,item):
        font = item.font()
        
        if item.checkState() == Qt.Checked:
            font.setStrikeOut(True)
        else:
            font.setStrikeOut(False)
        
        item.setFont(font)
            

        


window = MainWindow()
window.show()


sys.exit(app.exec())