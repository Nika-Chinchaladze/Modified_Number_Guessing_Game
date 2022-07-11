from PyQt5 import QtCore, QtGui, QtWidgets
from choose import Ui_Choose_page


class Ui_Welcome_page(object):

    def Choose_Window(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Choose_page()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, Welcome_page):
        Welcome_page.setObjectName("Welcome_page")
        Welcome_page.resize(376, 561)
        self.centralwidget = QtWidgets.QWidget(Welcome_page)
        self.centralwidget.setObjectName("centralwidget")
        
        self.hello_label = QtWidgets.QLabel(self.centralwidget)
        self.hello_label.setGeometry(QtCore.QRect(10, 10, 361, 151))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.hello_label.setFont(font)
        self.hello_label.setFrameShape(QtWidgets.QFrame.Box)
        self.hello_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hello_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hello_label.setWordWrap(True)
        self.hello_label.setObjectName("hello_label")
        
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(80, 470, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        
        self.picture_label = QtWidgets.QLabel(self.centralwidget)
        self.picture_label.setGeometry(QtCore.QRect(10, 180, 361, 271))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.picture_label.setFont(font)
        self.picture_label.setFrameShape(QtWidgets.QFrame.Box)
        self.picture_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.picture_label.setText("")
        self.picture_label.setPixmap(QtGui.QPixmap("guess.jpg"))
        self.picture_label.setScaledContents(True)
        self.picture_label.setAlignment(QtCore.Qt.AlignCenter)
        self.picture_label.setWordWrap(True)
        self.picture_label.setObjectName("picture_label")
        
        Welcome_page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Welcome_page)
        self.statusbar.setObjectName("statusbar")
        Welcome_page.setStatusBar(self.statusbar)

        self.retranslateUi(Welcome_page)
        QtCore.QMetaObject.connectSlotsByName(Welcome_page)

        # call Choose_Window From Here:
        self.start_button.clicked.connect(self.Choose_Window)
        self.start_button.clicked.connect(Welcome_page.close)

    def retranslateUi(self, Welcome_page):
        _translate = QtCore.QCoreApplication.translate
        Welcome_page.setWindowTitle(_translate("Welcome_page", "MainWindow"))
        self.hello_label.setText(_translate("Welcome_page", "Welcome To Number Guessing Game!"))
        self.start_button.setText(_translate("Welcome_page", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Welcome_page = QtWidgets.QMainWindow()
    ui = Ui_Welcome_page()
    ui.setupUi(Welcome_page)
    Welcome_page.show()
    sys.exit(app.exec_())
