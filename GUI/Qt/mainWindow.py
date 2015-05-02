from app.create_item import create_item
from app.update_item import update_item
from app.issue_item import issue_item
from app.show_items import show_items
from app.help import show_help


from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class mainWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QHBoxLayout()

        createItem = QPushButton("Create Item")
        updateItem = QPushButton("Update Item")
        issueItem = QPushButton("Issue Item")
        showItems = QPushButton("Show Items")
        help = QPushButton("Help")
        quit =QPushButton("Quit")

        layout.addWidget(createItem)
        layout.addWidget(updateItem)
        layout.addWidget(issueItem)
        layout.addWidget(showItems)
        layout.addWidget(help)
        layout.addWidget(quit)

        self.setLayout(layout)

        # Menu Event Handler
        createItem.clicked.connect(create_item)
        updateItem.clicked.connect(update_item)
        issueItem.clicked.connect(issue_item)
        showItems.clicked.connect(show_items)
        help.clicked.connect(show_help)
        quit.clicked.connect(self.close)


app = QApplication(sys.argv)
main_window = mainWindow()
main_window.show()
app.exec_()