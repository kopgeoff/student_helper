from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class PoemWidget(QWidget):
    def __init__(self):
        super().__init__()
        button = QPushButton("poem")
        f = QGridLayout()
        f.addWidget(button)
        self.setLayout(f)

