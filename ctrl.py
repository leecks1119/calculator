class Control:

    def __init__(self,view):
        self.view = view
        self.connectSignals()

    def calculate(self):
        num1 = float(self.view.le1.text())
        num2 = float(self.view.le2.text())
        operator = self.view.cb.currentText()

        if operator == '+':
            return f'{num1} + {num2} = {self.sum(num1, num2)}'
        else:
            return "Calculation Error"
        
        pass

    def connectSignals(self):
        self.view.btn1.clicked.connect(lambda:\
                                       self.view.setDisplay(self.calculate())) # 버튼 클릭 시 핸들러 함수 연결
        self.view.btn2.clicked.connect(self.view.clearMessage) # 버튼 2 클릭 시 핸들러 함수 연결

    def sum(sefl,a,b):
        try:
            return a+b
        except:
            return "Calculation Error"