import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
import random

# UI 로드
form_display1 = uic.loadUiType("display1.ui")[0]
form_display2 = uic.loadUiType("display2.ui")[0]
form_display3 = uic.loadUiType("display3.ui")[0]
form_display4 = uic.loadUiType("display4.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class display1(QDialog, QWidget, form_display1) : # 첫 번째 화면
    def __init__(self) :
        super(display1, self).__init__()
        self.setupUi(self)

        # '장비 구매' 버튼 클릭
        self.purchase_button.clicked.connect(self.start)

    def start(self):
        self.hide() # 현재 윈도우 숨기기
        self.close()
        self.start = display2() # 두 번째 화면 시작
        self.start.exec()
        self.show()


#화면을 띄우는데 사용되는 Class 선언
class display2(QDialog, QWidget, form_display2) : # 두 번째 화면
    def __init__(self) :
        super(display2,self).__init__()
        # self.setupUi(self)
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.purc_button.clicked.connect(self.next3)   # '구매' 버튼 클릭
        self.back_button.clicked.connect(self.before1) # '돌아가기' 버튼 클릭

    def next3(self):
        self.hide()  # 현재 윈도우 숨기기
        self.close()
        self.next3 = display4() # 세 번째 화면
        self.next3.exec()
        self.show()

    # '돌아가기' 누르면 display2 닫고, display 화면 뜨는 함수
    def before1(self):
        # self.close()
        self.hide()  # 현재 윈도우 숨기기
        self.close()
        self.before1 = display1()
        self.before1.exec_()
        self.show()
        self.show = display1()
        self.show()

# #화면을 띄우는데 사용되는 Class 선언
class display4(QDialog, QWidget, form_display4) : # 세 번째 화면
    def __init__(self) :
        super(display4,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.home_button.clicked.connect(self.next1)     # '메인화면으로' 버튼 클릭
        self.code_button.clicked.connect(self.give_code) # '코드 발급' 버튼 클릭
        self.ok_button.clicked.connect(self.give)        # '확인' 버튼 클릭

        no = str(random.randint(0,99999999)) # 구매 코드 0~99999999 사이 정수 랜덤하게 발급
        self.code_number.setText(no)

        #self.code_text.setText(self.code_number.toPlainText())
    def give_code(self):
        self.input_number.setText(self.code_number.toPlainText()) # '코드 발급' 버튼 누르면 label에 그대로 가져와서 보여주기

    def give(self):
        self.name_text.setText(self.input_name.toPlainText())     # '확인' 버튼 누르면 label에 이름 가져와서 보여주기
        self.code_text.setText(self.code_number.toPlainText())    # '확인' 버튼 누르면 label에 코드 가져와서 보여주기

    def next1(self):  # 첫 번째 화면으로 넘어가기
        self.hide()
        self.close()
        self.next1 = display1()
        self.next1.exec_()
        self.show()

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #display의 인스턴스 생성
    myWindow = display1()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
