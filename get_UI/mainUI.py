from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from get_UI import poemUI, noteUI, classUI, settingUI
import os

host = os.path.dirname(os.path.dirname(os.path.abspath("mainUI.py")))


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        desktop = QApplication.desktop()
        # 宽和高，经过多次测试获得，在测试机上看起来最舒服的一种大小
        width = int(desktop.width()*0.35)
        height = int(desktop.height()*0.88)
        # 不可变化大小
        self.setMaximumSize(QSize(width, height))
        self.setMinimumSize(QSize(width, height))
        # 显示位置
        self.move(QPoint(int(desktop.width()*0.60), int(desktop.height()*0.04)))
        # 使用palette来设置背景图片，但测试发现，在子widget中设置无效
        palette1 = QPalette()
        palette1.setColor(palette1.Background, QColor(245, 245, 245))
        palette1.setBrush(self.backgroundRole(),
                          QBrush(QPixmap(host + "/resources/test.png").scaled(self.width(), self.height())))
        # 上方的scaled是对图片自调整
        self.setPalette(palette1)
        self.setContentsMargins(0, 0, 0, 0)
        # 以上为设置主界面的位置、大小、背景等方法

        self.oneLayout = QVBoxLayout()
        self.oneLayout.setContentsMargins(0, 0, 0, 0)
        # 由于该布局中仅有两个widget，故设置占比为9：1
        self.oneLayout.setStretch(0, 9)
        self.oneLayout.setStretch(1, 1)
        self.oneLayout.setSpacing(0)
        # 第一层layout, 纵向

        self.twoLayout1 = QStackedLayout(self)
        self.twoLayout1.setContentsMargins(0, 0, 0, 0)

        # 下方四个分别来自于不同的Widget，用于界面设计的解耦
        self.one = poemUI.PoemWidget()
        self.two = classUI.ClassWidget()
        self.three = noteUI.NoteWidget()
        self.four = settingUI.SettingWidget()
        self.twoLayout1.addWidget(self.one)
        self.twoLayout1.addWidget(self.two)
        self.twoLayout1.addWidget(self.three)
        self.twoLayout1.addWidget(self.four)
        # 第二层上层layout，此为层叠布局，可根据下方按钮点击更换层叠布局

        self.twoLayout2 = QHBoxLayout()
        self.twoLayout2.setContentsMargins(0, 0, 0, 0)  # 布局内边距
        self.twoLayout2.setSpacing(0)
        # layout内组件间隔为0，但与实际情况不符合，仍会有一小部分的间隔

        # 构建按钮，绑定事件
        self.button1 = QPushButton("poem")
        self.button1.clicked.connect(lambda: self.show_widget(0))
        self.button1.setFixedSize(QSize(int(width / 4), int(height / 14)))
        self.button1.setStyleSheet("border:none;font-size:16px;font-weight:bold;")
        self.button2 = QPushButton("class")
        self.button2.clicked.connect(lambda: self.show_widget(1))
        self.button2.setFixedSize(QSize(int(width / 4), int(height / 14)))
        self.button2.setStyleSheet("border:none;font-size:16px;font-weight:bold;")
        self.button3 = QPushButton("note")
        self.button3.clicked.connect(lambda: self.show_widget(2))
        self.button3.setFixedSize(QSize(int(width / 4), int(height / 14)))
        self.button3.setStyleSheet("border:none;font-size:16px;font-weight:bold;")
        self.button4 = QPushButton("setting")
        self.button4.clicked.connect(lambda: self.show_widget(3))
        self.button4.setFixedSize(QSize(int(width / 4), int(height / 14)))
        self.button4.setStyleSheet("border:none;font-size:16px;font-weight:bold;")
        # 布局添加按钮
        self.twoLayout2.addWidget(self.button1)
        self.twoLayout2.addWidget(self.button2)
        self.twoLayout2.addWidget(self.button3)
        self.twoLayout2.addWidget(self.button4)
        # 第二层下层layout，用于放置层叠布局切换按钮

        self.twoWidget1 = QWidget()
        self.twoWidget1.setContentsMargins(0, 0, 0, 0)
        self.twoWidget2 = QWidget()
        # 设置下层layout的上边框显示，颜色和粗细待调整
        self.twoWidget2.setStyleSheet("border-top:2px solid;border-color:#79879D;")
        self.twoWidget2.setContentsMargins(0, 0, 0, 0)
        self.twoWidget1.setLayout(self.twoLayout1)
        self.twoWidget2.setLayout(self.twoLayout2)
        # 由于layout不可直接嵌套layout，故使用两个Widget来接受layout

        self.oneLayout.addWidget(self.twoWidget1)
        self.oneLayout.addWidget(self.twoWidget2)
        # 第一层添加第二层

        self.setLayout(self.oneLayout)
        # 主界面设置layout

        self.setWindowTitle("Hello Qt")
        # 在窗口初始化的时候加入就可以了
        # self.window是QMainWindow()
        self.show()
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 无边框，置顶
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 透明背景色

    def show_widget(self, index):
        self.twoLayout1.setCurrentIndex(index)
        # 在button绑定该事件时传入对应参数，即调用不同层叠布局


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = MainWidget()
    screen.show()
    sys.exit(app.exec_())
