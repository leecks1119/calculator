from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout
from PyQt5.QtGui import QIcon # icon을 추가하기 위한 라이브러리

class View(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
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