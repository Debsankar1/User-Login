# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import os

from PyQt5.QtWidgets import QApplication


class Ui_MainWindow(object):
    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.ok)
        mess.exec_()

    def submit(self):
        name=self.lineEdit.text()
        password=self.lineEdit_2.text()

        conn=pymysql.connect(host="Local instance MySQL80", user="root", password="Debmysql10@", db="alldatas")
        cur=conn.corsor()
        query=("INSERT INTO record(name, password)" "VALUES('%s', '%s')" % "(".join(name), ".join(password))")
        data=cur.execute(query, (name,password))

        print(data)
        if(data):
            self.messagebox("Congo!!", "You are Logged in!")






    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(455, 569)
        MainWindow.setMaximumSize(QtCore.QSize(455, 569))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 431, 555))
        self.frame.setMaximumSize(QtCore.QSize(433, 560))
        self.frame.setStyleSheet("image: url(:/login/close-up-photography-of-road-2453286.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(110, 230, 211, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 290, 151, 20))
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(150, 40, 131, 119))
        self.frame_2.setMaximumSize(QtCore.QSize(211, 119))
        self.frame_2.setStyleSheet("image: url(:/login/png-transparent-avatar-user-computer-icons-software-developer-avatar-child-face-heroes-thumbnail.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(180, 350, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.submit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 455, 21))
        self.menubar.setObjectName("menubar")
        self.menuOPPTIONS = QtWidgets.QMenu(self.menubar)
        self.menuOPPTIONS.setObjectName("menuOPPTIONS")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSIGN_UP = QtWidgets.QAction(MainWindow)
        self.actionSIGN_UP.setObjectName("actionSIGN_UP")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/login/download (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOptions.setIcon(icon)
        self.actionOptions.setObjectName("actionOptions")
        self.actionSign_up = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/login/6478-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSign_up.setIcon(icon1)
        self.actionSign_up.setObjectName("actionSign_up")
        self.menuOPPTIONS.addAction(self.actionOptions)
        self.menuOPPTIONS.addAction(self.actionSign_up)
        self.menubar.addAction(self.menuOPPTIONS.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "PLEASE ENTER THE USER ID!!"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "PASSWORD !!"))
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))
        self.menuOPPTIONS.setTitle(_translate("MainWindow", "Menu"))
        self.actionSIGN_UP.setText(_translate("MainWindow", "SIGN UP"))
        self.actionOptions.setText(_translate("MainWindow", "Options"))
        self.actionSign_up.setText(_translate("MainWindow", "Sign up"))
import login_rc


def update_title(self):
    self.setWindowTitle("%s - Login" % (os.path.basename(self.path) if self.path else "LOGIN "))

if __name__ == "__main__":
    import sys






    app = QtWidgets.QApplication(sys.argv)
   
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
