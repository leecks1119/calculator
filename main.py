import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon # icon을 추가하기 위한 라이브러리

class Calculator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.btn1=QPushButton('Message',self) # 버튼추가
        self.btn1.clicked.connect(self.activateMessage) # 버튼 클릭 시 핸들러 함수 연결

        vbox=QVBoxLayout() # 수직 레이아웃 위젯 생성
        vbox.addStretch(1) # 빈 공간
        vbox.addWidget(self.btn1)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256, 256)
        self.show()
        
    def activateMessage(self):
        QMessageBox.information(self,"informatino","Button clicked!")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())