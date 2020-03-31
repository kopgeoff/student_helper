from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        desktop = QApplication.desktop()
        self.setMaximumSize(QSize(int(desktop.width()*0.35), int(desktop.height()*0.88)))
        self.setMinimumSize(QSize(int(desktop.width()*0.35), int(desktop.height()*0.88)))
        self.move(QPoint(int(desktop.width()*0.60), int(desktop.height()*0.04)))
        tmp = QWebEngineView()

        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(tmp)

        mainLayout = QGridLayout()
        mainLayout.addLayout(buttonLayout1, 1, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Hello Qt")
        tmp.load(QUrl('D:/personal/index.html'))
        tmp.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = Form()
    screen.show()
    sys.exit(app.exec_())