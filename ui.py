from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout, QLineEdit, QComboBox
from PyQt5.QtGui import QIcon # icon을 추가하기 위한 라이브러리
from PyQt5 import QtCore

class View(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn1=QPushButton('Calc',self) # 버튼추가
        self.btn2=QPushButton('Clear',self) # 버튼2 추가

        self.te1=QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.le1=QLineEdit('0',self)
        self.le1.setAlignment(QtCore.Qt.AlignRight)
        self.le1.setFocus(True)
        self.le1.selectAll()

        self.le2=QLineEdit('0',self)
        self.le2.setAlignment(QtCore.Qt.AlignRight)

        self.cb=QComboBox(self)
        self.cb.addItems(['+', '-', '*', '/', '^']) #거듭제곱 연산자 추가

        hbox_formular = QHBoxLayout()
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox=QVBoxLayout() # 수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256, 256)
        self.show()

    def setDisplay(self,text):
        self.te1.appendPlainText(text)

    def clearMessage(self):
        # QMessageBox.information(self,"informatino","Button clicked!")
        self.te1.clear()