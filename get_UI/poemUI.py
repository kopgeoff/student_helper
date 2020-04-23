from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


urls = "./resources/1.jpg"
qss = "#Poem{border-image: url(%s);}" % urls


class PoemWidget(QWidget):
    def __init__(self):
        super().__init__()
        button = QPushButton("poem")
        f = QGridLayout()
        f.addWidget(button)
        self.setLayout(f)
        self.setObjectName("Poem")
        self.setStyleSheet("#Poem{background-color:#bbddf0}")

    def paintEvent(self, a0: QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        # painter.setRenderHint(QtGui.QPainter.Antialiasing) # 反锯齿
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
