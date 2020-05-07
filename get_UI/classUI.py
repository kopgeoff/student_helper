from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from get_database import sqlitedatabase


class ClassWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Class")
        self.setStyleSheet("#Class{background-color:#bbddf0}")
        self.twoLayout1 = QStackedLayout()
        self.table = QTableWidget(14, 7)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setHorizontalHeaderLabels(["星期日","星期一","星期二","星期三","星期四","星期五","星期六"])
        self.table.setVerticalHeaderLabels(["","第一节","第二节","第三节",
                            "第四节","第五节","第六节","第七节","第八节","第九节","第十节","第十一节","第十二节",""])
        desktop = QApplication.desktop()
        # 宽和高，经过多次测试获得，在测试机上看起来最舒服的一种大小
        width = int(desktop.width() * 0.35)
        self.table.setColumnWidth(0, int(width / 8.3))
        self.table.setColumnWidth(1, int(width / 8.3))
        self.table.setColumnWidth(2, int(width / 8.3))
        self.table.setColumnWidth(3, int(width / 8.3))
        self.table.setColumnWidth(4, int(width / 8.3))
        self.table.setColumnWidth(5, int(width / 8.3))
        self.table.setColumnWidth(6, int(width / 8.3))
        self.table.setRowHeight(1, int(width / 11))
        self.table.setRowHeight(2, int(width / 11))
        self.table.setRowHeight(3, int(width / 11))
        self.table.setRowHeight(4, int(width / 11))
        self.table.setRowHeight(5, int(width / 11))
        self.table.setRowHeight(6, int(width / 11))
        self.table.setRowHeight(7, int(width / 11))
        self.table.setRowHeight(8, int(width / 11))
        self.table.setRowHeight(9, int(width / 11))
        self.table.setRowHeight(10, int(width / 11))
        self.table.setRowHeight(11, int(width / 11))
        self.table.setRowHeight(12, int(width / 11))
        for i in range(1, 12, 2):
            for j in range(7):
                self.table.setSpan(i,j,2,1)
        self.table.setSpan(13,0,1,7)
        bottom_widget = QWidget()
        button = QPushButton("添加课程")
        button.clicked.connect(lambda: self.show_widget(1))
        button1 = QPushButton("删除课程")
        button1.clicked.connect(lambda: self.show_widget(2))
        button.setFixedHeight(int(width / 20))
        button1.setFixedHeight(int(width / 20))
        layout1 = QHBoxLayout()
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.addWidget(button)
        layout1.addWidget(button1)
        bottom_widget.setLayout(layout1)
        self.table.setCellWidget(13,0,bottom_widget)
        self.flag = 0
        self.combobox = QComboBox()
        for i in range(53):
            self.combobox.addItem("第"+str(i)+"周")
        self.combobox.currentIndexChanged.connect(self.changeclass)
        layout1.addWidget(self.combobox)

        w = QWidget()
        two_widget = QVBoxLayout()
        wid1 = QWidget()
        widget1 = QHBoxLayout()
        label1 = QLabel("请输入课程名：")
        self.line1 = QLineEdit()
        widget1.addWidget(label1)
        widget1.addWidget(self.line1)
        wid1.setLayout(widget1)

        wid2 = QWidget()
        widget2 = QHBoxLayout()
        label2 = QLabel("请输入教室：")
        self.line2 = QLineEdit()
        widget2.addWidget(label2)
        widget2.addWidget(self.line2)
        wid2.setLayout(widget2)

        wid3 = QWidget()
        widget3 = QHBoxLayout()
        label3 = QLabel("请输入上课周数：")
        self.line3 = QLineEdit()
        label4 = QLabel("--")
        self.line4 = QLineEdit()
        widget3.addWidget(label3)
        widget3.addWidget(self.line3)
        widget3.addWidget(label4)
        widget3.addWidget(self.line4)
        wid3.setLayout(widget3)

        wid4 = QWidget()
        widd4 = QHBoxLayout()
        label5 = QLabel("上课节数：")
        self.widget4 = QComboBox()
        for i in range(1, 13, 2):
            self.widget4.addItem(str(i)+"-"+str(i+1)+"节")
        self.widget5 = QComboBox()
        self.widget5.addItem("星期日")
        self.widget5.addItem("星期一")
        self.widget5.addItem("星期二")
        self.widget5.addItem("星期三")
        self.widget5.addItem("星期四")
        self.widget5.addItem("星期五")
        self.widget5.addItem("星期六")
        widd4.addWidget(label5)
        widd4.addWidget(self.widget4)
        widd4.addWidget(self.widget5)
        wid4.setLayout(widd4)

        wi5 = QWidget()
        func = QHBoxLayout()
        back = QPushButton("返回")
        back.clicked.connect(self.show_class)
        next = QPushButton("确定")
        next.clicked.connect(self.add_delete)
        func.addWidget(back)
        func.addWidget(next)
        wi5.setLayout(func)
        two_widget.addWidget(wid1)
        two_widget.addWidget(wid2)
        two_widget.addWidget(wid3)
        two_widget.addWidget(wid4)
        two_widget.addWidget(wi5)
        w.setLayout(two_widget)
        self.twoLayout1.addWidget(self.table)
        self.twoLayout1.addWidget(w)
        self.setLayout(self.twoLayout1)


    def paintEvent(self, a0: QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        # painter.setRenderHint(QtGui.QPainter.Antialiasing) # 反锯齿
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)

    def show_widget(self, index):
        self.twoLayout1.setCurrentIndex(1)
        # 在button绑定该事件时传入对应参数，即调用不同层叠布局
        self.flag = index
        if index == 1:
            self.line1.setEnabled(True)
            self.line2.setEnabled(True)
            self.line3.setEnabled(True)
            self.line4.setEnabled(True)
            self.widget4.setEnabled(True)
            self.widget5.setEnabled(True)
        else:
            self.line1.setEnabled(True)
            self.line2.setEnabled(False)
            self.line3.setEnabled(False)
            self.line4.setEnabled(False)
            self.widget4.setEnabled(False)
            self.widget5.setEnabled(False)

    def show_class(self):
        self.twoLayout1.setCurrentIndex(0)
        # 在button绑定该事件时传入对应参数，即调用不同层叠布局

    def changeclass(self):
        self.clearclass()
        value = self.combobox.currentIndex()
        classplan = sqlitedatabase.getclass(value)
        for k in classplan:
            s = k[0]+"\n"+k[3]
            week = int(int(k[1]) / 12)
            posi = int(k[1]) % 12
            label = QLabel(s)
            self.table.setCellWidget(posi, week, label)

    def clearclass(self):
        for i in range(7):
            for j in range(1, 13, 2):
                self.table.removeCellWidget(j, i)

    def add_delete(self):
        if self.flag == 1:
            cname = self.line1.text()
            pname = self.line2.text()
            start = self.line3.text()
            end = self.line4.text()
            posi = 2*self.widget4.currentIndex()+1+12*self.widget5.currentIndex()
            s = ["0"]*53
            for i in range(int(start), int(end)+1):
                s[i] = "1"
            s = "".join(s)
            if sqlitedatabase.add_item(cname,posi,s,pname):
                self.changeclass()

            self.show_class()

        else:
            cname = self.line1.text()
            if sqlitedatabase.delete_item(cname):
                self.changeclass()

            self.show_class()

