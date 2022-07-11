from PyQt5 import QtCore, QtGui, QtWidgets
from game import Ui_Game_page
from math import log
from random import randint


class Ui_Choose_page(object):

    def Game_Window(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = Ui_Game_page()
        self.ui.setupUi(self.window3)
        self.window3.show()

    def setupUi(self, Choose_page):
        Choose_page.setObjectName("Choose_page")
        Choose_page.resize(376, 561)
        self.centralwidget = QtWidgets.QWidget(Choose_page)
        self.centralwidget.setObjectName("centralwidget")
        
        self.hello_label = QtWidgets.QLabel(self.centralwidget)
        self.hello_label.setGeometry(QtCore.QRect(10, 10, 361, 131))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.hello_label.setFont(font)
        self.hello_label.setFrameShape(QtWidgets.QFrame.Box)
        self.hello_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hello_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hello_label.setWordWrap(True)
        self.hello_label.setObjectName("hello_label")

        self.enter_low_bound = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_low_bound.setGeometry(QtCore.QRect(42, 390, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_low_bound.setFont(font)
        self.enter_low_bound.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_low_bound.setObjectName("enter_low_bound")
        
        self.enter_up_bound = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_up_bound.setGeometry(QtCore.QRect(220, 390, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_up_bound.setFont(font)
        self.enter_up_bound.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_up_bound.setObjectName("enter_up_bound")
        
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(80, 470, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.submit_button.setFont(font)
        self.submit_button.setStyleSheet("background-color: rgb(0, 175, 175);")
        self.submit_button.setObjectName("submit_button")
        
        self.lower_bound = QtWidgets.QLabel(self.centralwidget)
        self.lower_bound.setGeometry(QtCore.QRect(40, 350, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lower_bound.setFont(font)
        self.lower_bound.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lower_bound.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lower_bound.setAlignment(QtCore.Qt.AlignCenter)
        self.lower_bound.setWordWrap(True)
        self.lower_bound.setObjectName("lower_bound")
        
        self.upper_bound = QtWidgets.QLabel(self.centralwidget)
        self.upper_bound.setGeometry(QtCore.QRect(220, 350, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.upper_bound.setFont(font)
        self.upper_bound.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.upper_bound.setFrameShadow(QtWidgets.QFrame.Raised)
        self.upper_bound.setAlignment(QtCore.Qt.AlignCenter)
        self.upper_bound.setWordWrap(True)
        self.upper_bound.setObjectName("upper_bound")
        
        self.picture_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.picture_label_2.setGeometry(QtCore.QRect(10, 160, 361, 181))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.picture_label_2.setFont(font)
        self.picture_label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.picture_label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.picture_label_2.setText("")
        self.picture_label_2.setPixmap(QtGui.QPixmap("chosen.jpg"))
        self.picture_label_2.setScaledContents(True)
        self.picture_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.picture_label_2.setWordWrap(True)
        self.picture_label_2.setObjectName("picture_label_2")        
        
        Choose_page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Choose_page)
        self.statusbar.setObjectName("statusbar")
        Choose_page.setStatusBar(self.statusbar)

        self.retranslateUi(Choose_page)
        QtCore.QMetaObject.connectSlotsByName(Choose_page)
# ------------------------------------------ LOGIC ------------------------------------------- #
        # call some functions from here:
        self.submit_button.clicked.connect(self.Game_Window)
        self.submit_button.clicked.connect(self.Write_next)
        self.submit_button.clicked.connect(Choose_page.close)

    # define method for range label in the next page:
    def Write_next(self):
        # range label:
        lower_screen = self.enter_low_bound.text()
        upper_screen = self.enter_up_bound.text()

        if len(lower_screen) != 0 and len(upper_screen) != 0:
            if int(lower_screen) < int(upper_screen):
                self.ui.appear_range_label.setText(f'[{lower_screen} : {upper_screen}]')
                # best minimum tries label:
                best = round(log(int(upper_screen) - int(lower_screen) + 1))
                self.ui.num_min_try.setText(f'{best}')
                # Maximum Tries:
                self.ui.num_max_try.setText(f'{best + best}')
                # Random number between Range: Chosen by Computer
                Computer_thought = randint(int(lower_screen), int(upper_screen))
                self.ui.secret_label.setText(f'{Computer_thought}')
            
            elif int(lower_screen) >= int(upper_screen):
                self.ui.message_label.setText("Range Was Not Defined Correctly!")
                self.ui.message_label.setStyleSheet("background-color: rgb(255, 35, 35);")
                self.ui.check_button.setEnabled(False)
        
        # if range was not defined correctly by player:
        elif len(lower_screen) == 0 or len(upper_screen) == 0:
            self.ui.message_label.setText("Range Was Not Defined Correctly!")
            self.ui.message_label.setStyleSheet("background-color: rgb(255, 35, 35);")
            self.ui.check_button.setEnabled(False)

        
# ------------------------------------------- END ------------------------------------------- #

    def retranslateUi(self, Choose_page):
        _translate = QtCore.QCoreApplication.translate
        Choose_page.setWindowTitle(_translate("Choose_page", "MainWindow"))
        self.hello_label.setText(_translate("Choose_page", "Choose The Range!"))
        self.submit_button.setText(_translate("Choose_page", "Submit"))
        self.lower_bound.setText(_translate("Choose_page", "Lower Bound"))
        self.upper_bound.setText(_translate("Choose_page", "Upper Bound"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Choose_page = QtWidgets.QMainWindow()
    ui = Ui_Choose_page()
    ui.setupUi(Choose_page)
    Choose_page.show()
    sys.exit(app.exec_())
