from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import requests
from get_poem import getOnePoem


class PoemWidget(QWidget):
    def __init__(self):
        super().__init__()
        fontId = QFontDatabase.addApplicationFont("./fonts/汉仪糯米团简.ttf")
        fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
        label = QLabel(getOnePoem.get_poem())
        label.setStyleSheet("font-size:30px;")
        label.setFont(QFont(fontName))
        self.setObjectName("Poem")
        self.setStyleSheet("#Poem{background-color:#bbddf0}")
        url = getOnePoem.get_image()
        if url != "":
            req = requests.get(url)
            image = req.content
            req.close()
            f = open("temp.jpg", "wb")
            f.write(image)
            f.close()
            self.setStyleSheet("#Poem{background-color:#bbddf0; background-image:url('./temp.jpg');}")
        f = QGridLayout()

        f.addWidget(label)
        self.setLayout(f)

    def paintEvent(self, a0: QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        # painter.setRenderHint(QtGui.QPainter.Antialiasing) # 反锯齿
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
