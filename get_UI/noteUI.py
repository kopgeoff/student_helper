from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from get_database import sqlitedatabase


class NoteWidget(QWidget):
    def __init__(self):
        super().__init__()
        f = QGridLayout()
        self.setLayout(f)
        self.setObjectName("Note")
        self.setStyleSheet("#Note{background-color:#bbddf0}")
        #button = QPushButton("保存到本地")
        #button.clicked.connect(self.update_note)
        self.table = QTableWidget(25, 1)
        desktop = QApplication.desktop()
        # 宽和高，经过多次测试获得，在测试机上看起来最舒服的一种大小
        width = int(desktop.width() * 0.35)
        self.table.setHorizontalHeaderLabels(["想要添加备忘录，双击空白单元格即可。"])
        self.table.setColumnWidth(0, int(width))
        for i in range(25):
            self.table.setRowHeight(i, int(width / 11))
        self.load_note()
        self.table.cellChanged.connect(self.update_note)
        #f.addWidget(button)
        f.addWidget(self.table)

    def paintEvent(self, a0: QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        # painter.setRenderHint(QtGui.QPainter.Antialiasing) # 反锯齿
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)

    def load_note(self):
        data = sqlitedatabase.load_note()
        for i in range(len(data)):
            self.table.setItem(i,0,QTableWidgetItem(data[i][0]))

    def update_note(self):
        data = []
        for i in range(25):
            s = ""
            try:
                s = self.table.item(i,0).text()
            except:
                s = ""
            finally:
                data.append(s)
        sqlitedatabase.update_note(data)


