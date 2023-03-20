from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
                             QMessageBox, QPlainTextEdit, QHBoxLayout, QLabel)
from PyQt5.QtGui import QIcon # icon을 추가하기 위한 라이브러리
from PyQt5.QtCore import QDate, Qt # 날짜와 주요 속성값 사용을 위해 추가

class View(QWidget):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel(self.date.toString(Qt.DefaultLocaleLongDate),self)
        self.btn1=QPushButton('Message',self) # 버튼추가
        self.btn2=QPushButton('Clear',self) # 버튼2 추가

        self.te1=QPlainTextEdit()
        self.te1.setReadOnly(True)

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox=QVBoxLayout() # 수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox)
        vbox.addWidget(self.lbl1)
        
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256, 256)
        self.show()

    def activateMessage(self):
        # QMessageBox.information(self,"informatino","Button clicked!")
        self.te1.appendPlainText("Button clicked!")

    def clearMessage(self):
        # QMessageBox.information(self,"informatino","Button clicked!")
        self.te1.clear()