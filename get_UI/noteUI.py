from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class NoteWidget(QWidget):
    def __init__(self):
        super().__init__()
        button = QPushButton("note")
        f = QGridLayout()
        f.addWidget(button)
        self.setLayout(f)