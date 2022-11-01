# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HP\Desktop\KBscan\Application_Photo_scan_BD\App_photo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#vide
# WARNING! All changes made in this file will be lost!
import res_rc

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from App_photo_Affichage import Affichage
class Ui_MainWindow(object):
    def logout(self):
        self.aff.close()
        MainWindow.show()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.ui.mydb.close()
    def Afficher(self,curs):
        self.Affiche = QtWidgets.QMainWindow()
        self.ui = Affichage() 
        self.ui.setupUi(self.Affiche,curs)
        self.ui.pushButton_6.clicked.connect(lambda: self.logout())
        return self.Affiche
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(493, 476)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-30, -10, 591, 521))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("border-image: url(:/image/background.jpg);\n"
"border-top-left-radius : 50px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label_2.setStyleSheet("background-color: rgba(0,0,0,80);\n"
"border-top-left-radius : 50px;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(270, 30, 240, 430))
        self.label_3.setStyleSheet("background-color: rgba(255,255,255,255);\n"
"border-bottom-right-radius : 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(320, 60, 150, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(100)
        font.setFamily("Garamond")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgba(0,0,0,200);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(295, 150, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Garamond")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(295, 215, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Garamond")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.returnPressed.connect(self.login)
        self.pushButton = QtWidgets.QPushButton(self.widget,clicked = lambda : self.login())
        #self.pushButton.setDefault(True)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setGeometry(QtCore.QRect(295, 300, 190, 40))
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"background-color: rgba(11, 131, 120, 219);\n"
"color: rgba(255, 255, 255, 210);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"background-color: rgba(150, 123, 111, 219);\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(290, 360, 191, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color: rgba(0, 0, 0 ,0);\n"
"color: rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgba(131, 96, 53, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color:rgba(91,88,53,255);\n"
"}\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: rgba(0, 0, 0 ,0);\n"
"color: rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgba(131, 96, 53, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color:rgba(91,88,53,255);\n"
"}\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgba(0, 0, 0 ,0);\n"
"color: rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgba(131, 96, 53, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color:rgba(91,88,53,255);\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"background-color: rgba(0, 0, 0 ,0);\n"
"color: rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgba(131, 96, 53, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color:rgba(91,88,53,255);\n"
"}\n"
"\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def login(self):
        user_name = self.lineEdit.text()
        password_ = self.lineEdit_2.text()
        cursor = None
        try:
            # Creating connection object
            mydb = mysql.connector.connect(
                host = "localhost",
                user = user_name,
                password = password_,
                autocommit=True,
                database='test',
            )
            
            cursor = mydb.cursor(buffered=True)
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Erreur")
            msg.setText("Veuillez entrez un nom d'utilisateur/mot de passe valide")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setTextFormat(QtCore.Qt.RichText)
            msg.resize(msg.sizeHint())
            x = msg.exec_()
        if cursor!=None:
            self.aff = self.Afficher(mydb)
            self.aff.show()
            MainWindow.hide()
                
          
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Se Connecter"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", " Nom d'utilisateur"))
        self.lineEdit.setText("youssef")
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", " Mot de passe"))
        self.lineEdit_2.setText("kbscan123*")
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_4.setText(_translate("MainWindow", "Q"))
        self.pushButton_3.setText(_translate("MainWindow", "E"))
        self.pushButton_2.setText(_translate("MainWindow", "C"))
        self.pushButton_5.setText(_translate("MainWindow", "¥p"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

