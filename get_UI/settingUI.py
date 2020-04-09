from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class SettingWidget(QWidget):
    def __init__(self):
        super().__init__()
        button = QPushButton("setting")
        f = QGridLayout()
        f.addWidget(button)
        self.setLayout(f)

