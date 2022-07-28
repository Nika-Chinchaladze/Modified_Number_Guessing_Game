from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Game_page(object):

    def Play_Again(self):
        from choose import Ui_Choose_page

        self.window2big = QtWidgets.QMainWindow()
        self.play = Ui_Choose_page()
        self.play.setupUi(self.window2big)
        self.window2big.show()

    def setupUi(self, Game_page):
        Game_page.setObjectName("Game_page")
        Game_page.resize(380, 600)
        self.centralwidget = QtWidgets.QWidget(Game_page)
        self.centralwidget.setObjectName("centralwidget")

        self.Msg_button = QtWidgets.QPushButton(self.centralwidget)
        self.Msg_button.setGeometry(QtCore.QRect(10, 435, 359, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Msg_button.setFont(font)
        self.Msg_button.setStyleSheet("background-color: rgb(198, 198, 148);")
        self.Msg_button.setObjectName("Msg_button")
        self.Msg_button.setEnabled(False)
        
        self.try_button = QtWidgets.QPushButton(self.centralwidget)
        self.try_button.setGeometry(QtCore.QRect(10, 487, 359, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.try_button.setFont(font)
        self.try_button.setStyleSheet("background-color: rgb(119, 240, 178);")
        self.try_button.setObjectName("try_button")

        self.end_button = QtWidgets.QPushButton(self.centralwidget)
        self.end_button.setGeometry(QtCore.QRect(10, 537, 359, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.end_button.setFont(font)
        self.end_button.setStyleSheet("background-color: rgb(125, 188, 188);")
        self.end_button.setObjectName("end_button")
        
        self.min_try_label = QtWidgets.QLabel(self.centralwidget)
        self.min_try_label.setGeometry(QtCore.QRect(10, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.min_try_label.setFont(font)
        self.min_try_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.min_try_label.setObjectName("min_try_label")

#-----  # secret label, this label won't appear on the screen and hold the number chosen by Computer: ------------------- #
        self.secret_label = QtWidgets.QLabel(self.centralwidget)
        self.secret_label.setGeometry(QtCore.QRect(330, 10, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.secret_label.setFont(font)
        self.secret_label.setStyleSheet("color: rgb(240, 240, 240);")
        self.secret_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.secret_label.setObjectName("secret_label")
# -------------------------------------------------------------------------------------------------------- #
        
        self.current_tries_label = QtWidgets.QLabel(self.centralwidget)
        self.current_tries_label.setGeometry(QtCore.QRect(10, 110, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.current_tries_label.setFont(font)
        self.current_tries_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.current_tries_label.setObjectName("current_tries_label")
        
        self.max_tries_label = QtWidgets.QLabel(self.centralwidget)
        self.max_tries_label.setGeometry(QtCore.QRect(10, 60, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.max_tries_label.setFont(font)
        self.max_tries_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.max_tries_label.setObjectName("max_tries_label")
        
        self.range_label = QtWidgets.QLabel(self.centralwidget)
        self.range_label.setGeometry(QtCore.QRect(10, 160, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.range_label.setFont(font)
        self.range_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.range_label.setObjectName("range_label")
        
        self.message_label = QtWidgets.QLabel(self.centralwidget)
        self.message_label.setGeometry(QtCore.QRect(10, 210, 361, 131))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.message_label.setFont(font)
        self.message_label.setFrameShape(QtWidgets.QFrame.Box)
        self.message_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.message_label.setText("")
        self.message_label.setAlignment(QtCore.Qt.AlignCenter)
        self.message_label.setWordWrap(True)
        self.message_label.setObjectName("message_label")
        
        self.num_min_try = QtWidgets.QLabel(self.centralwidget)
        self.num_min_try.setGeometry(QtCore.QRect(150, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.num_min_try.setFont(font)
        self.num_min_try.setFrameShape(QtWidgets.QFrame.Box)
        self.num_min_try.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.num_min_try.setText("")
        self.num_min_try.setAlignment(QtCore.Qt.AlignCenter)
        self.num_min_try.setObjectName("num_min_try")
        
        self.num_max_try = QtWidgets.QLabel(self.centralwidget)
        self.num_max_try.setGeometry(QtCore.QRect(180, 60, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.num_max_try.setFont(font)
        self.num_max_try.setFrameShape(QtWidgets.QFrame.Box)
        self.num_max_try.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.num_max_try.setText("")
        self.num_max_try.setAlignment(QtCore.Qt.AlignCenter)
        self.num_max_try.setObjectName("num_max_try")
        
        self.num_current_try = QtWidgets.QLabel(self.centralwidget)
        self.num_current_try.setGeometry(QtCore.QRect(210, 110, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.num_current_try.setFont(font)
        self.num_current_try.setFrameShape(QtWidgets.QFrame.Box)
        self.num_current_try.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.num_current_try.setText("")
        self.num_current_try.setAlignment(QtCore.Qt.AlignCenter)
        self.num_current_try.setObjectName("num_current_try")
        
        self.appear_range_label = QtWidgets.QLabel(self.centralwidget)
        self.appear_range_label.setGeometry(QtCore.QRect(80, 160, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.appear_range_label.setFont(font)
        self.appear_range_label.setFrameShape(QtWidgets.QFrame.Box)
        self.appear_range_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.appear_range_label.setText("")
        self.appear_range_label.setAlignment(QtCore.Qt.AlignCenter)
        self.appear_range_label.setObjectName("appear_range_label")
        
        self.instruction_label = QtWidgets.QLabel(self.centralwidget)
        self.instruction_label.setGeometry(QtCore.QRect(20, 350, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.instruction_label.setFont(font)
        self.instruction_label.setAlignment(QtCore.Qt.AlignCenter)
        self.instruction_label.setObjectName("instruction_label")
        
        self.Enter_Number_Place = QtWidgets.QLineEdit(self.centralwidget)
        self.Enter_Number_Place.setGeometry(QtCore.QRect(10, 380, 151, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Enter_Number_Place.setFont(font)
        self.Enter_Number_Place.setText("")
        self.Enter_Number_Place.setAlignment(QtCore.Qt.AlignCenter)
        self.Enter_Number_Place.setObjectName("Enter_Number_Place")
        
        self.check_button = QtWidgets.QPushButton(self.centralwidget)
        self.check_button.setGeometry(QtCore.QRect(214, 380, 155, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.check_button.setFont(font)
        self.check_button.setStyleSheet("background-color: rgb(84, 252, 123);")
        self.check_button.setObjectName("check_button")
        # from here we will be able to count clicks on check button = count player's tries:
        self.Counter = 0
        
        # define List of Entered Numbers, which will be displayed in the Message Box Window:
        self.Entered_Numbers_List = []
        
        Game_page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Game_page)
        self.statusbar.setObjectName("statusbar")
        Game_page.setStatusBar(self.statusbar)

        self.retranslateUi(Game_page)
        QtCore.QMetaObject.connectSlotsByName(Game_page)

# ------------------------------------------ LOGIC ------------------------------------------- #
        # call some functions from here:
        self.end_button.clicked.connect(Game_page.close)
        self.Msg_button.clicked.connect(self.show_box)
        self.check_button.clicked.connect(self.check_number)
        self.try_button.clicked.connect(self.Play_Again)
        self.try_button.clicked.connect(Game_page.close)
    
    # define method for check button:
    def check_number(self):
        try:
            self.Counter += 1
            self.num_current_try.setText(f'{self.Counter}')

            random_number = int(self.secret_label.text())
            Entered_Number = int(self.Enter_Number_Place.text())

            # let's append Entered_Numbers List Here:
            self.Entered_Numbers_List.append(Entered_Number)

        
            if Entered_Number == random_number:
                if self.Counter <= int(self.num_min_try.text()):
                    self.message_label.setText(f'Best Play Ever Seen! Congratulations You Won The Game In - {self.Counter} Try!')
                    self.message_label.setStyleSheet("QLabel" "{" "background : lightgreen;" "}")
                    self.check_button.setEnabled(False)
                    self.Msg_button.setEnabled(True)
                elif self.Counter > int(self.num_min_try.text()) and self.Counter <= int(self.num_max_try.text()):
                    self.message_label.setText(f'Correct Guess! Congratulations You Won The Game In - {self.Counter} Try!')
                    self.message_label.setStyleSheet("background-color: rgb(170, 255, 255);")
                    self.check_button.setEnabled(False)
                    self.Msg_button.setEnabled(True)
            elif Entered_Number < random_number:
                self.message_label.setText("Entered Number is Smaller, Increase!")
                self.message_label.setStyleSheet("background-color: rgb(234, 234, 116);")
            elif Entered_Number > random_number:
                self.message_label.setText("Entered Number is Bigger, Reduce!")
                self.message_label.setStyleSheet("background-color: rgb(200, 200, 200);")
            
            # Player will lose if Number of tries ar too high:
            critical_number = int(self.num_max_try.text())
            if self.Counter == (critical_number + 1):
                self.message_label.setText(f'You Lose! Number Of Tries were Too High: {self.Counter}')
                self.message_label.setStyleSheet("background-color: rgb(255, 35, 35);")
                self.check_button.setEnabled(False)
                self.Msg_button.setEnabled(True)
        except:
            self.message_label.setText("Enter Number!")
        
    # define method for Message Box button:
    def show_box(self, i):
        msg = QMessageBox()
        msg.setWindowTitle("Entered Numbers!")
        msg.setText(f'Number Chosen By Computer: {int(self.secret_label.text())}' )
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Cancel)
        msg.setInformativeText("Numbers Entered By Player!")
        msg.setDetailedText(f'{self.Entered_Numbers_List}')

        x = msg.exec_()

# ------------------------------------------- END ------------------------------------------- #

    def retranslateUi(self, Game_page):
        _translate = QtCore.QCoreApplication.translate
        Game_page.setWindowTitle(_translate("Game_page", "MainWindow"))
        self.Msg_button.setText(_translate("Game_page", "Message Box"))
        self.try_button.setText(_translate("Game_page", "Play Again"))
        self.end_button.setText(_translate("Game_page", "End The Game!"))
        self.min_try_label.setText(_translate("Game_page", "Min Tries To Win:"))
        self.current_tries_label.setText(_translate("Game_page", "Numbers of Current Tries:"))
        self.max_tries_label.setText(_translate("Game_page", "Number Of Max Tries:"))
        self.range_label.setText(_translate("Game_page", "Range:"))
        self.instruction_label.setText(_translate("Game_page", "Enter The Number!"))
        self.check_button.setText(_translate("Game_page", "Check"))
        self.secret_label.setText(_translate("Game_page", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Game_page = QtWidgets.QMainWindow()
    ui = Ui_Game_page()
    ui.setupUi(Game_page)
    Game_page.show()
    sys.exit(app.exec_())
