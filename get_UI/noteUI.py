from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


urls = "./resources/1.jpg"
qss = "#Note{border-image: url(%s);}" % urls


class NoteWidget(QWidget):
    def __init__(self):
        super().__init__()
        button = QPushButton("note")
        f = QGridLayout()
        f.addWidget(button)
        self.setLayout(f)
        self.setObjectName("Note")
        self.setStyleSheet("#Note{background-color:#bbddf0}")

    def paintEvent(self, a0: QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        # painter.setRenderHint(QtGui.QPainter.Antialiasing) # 反锯齿
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
