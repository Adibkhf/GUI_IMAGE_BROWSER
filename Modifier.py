# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HP\Desktop\KBscan\Application_Photo_scan_BD\App_photo_Affichage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

class Modifier_ligne(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Modification")
        MainWindow.setFixedSize(672, 496)
        MainWindow.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QWidget{\n"
"border : solid 10 px rgba(0,0,0);\n"
"background-color :#eee;\n"
"    }\n"
"\n"
"QLabel{\n"
"background-color:rgba(0,0,0,0%);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QLineEdit{\n"
"border-radius:10px;\n"
"border: 1px solid rgb(0, 0, 0);\n"
"background-color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QDateEdit{\n"
"border-radius:10px;\n"
"border: 1px solid rgb(0, 0, 0);\n"
"background-color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"background-color: rgba(11, 131, 120, 219);\n"
"color: rgba(255, 255, 255, 210);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(150, 123, 111, 219);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"\n"
"QTextEdit:focus{\n"
" border:2px solid rgba(150, 123, 111, 219);\n"
"\n"
"}\n"
"QComboBox{\n"
"background : #55d1d3;\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"background-color:rgb(255, 255, 255)\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-300, -100, 991, 691))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.label.setText("")
        self.pixmap = QPixmap('bc2.jpg')
 
        # adding image to label
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 180, 171, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.LineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit_7.setEnabled(True)
        self.LineEdit_7.setGeometry(QtCore.QRect(300, 100, 360, 35))        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineEdit_7.sizePolicy().hasHeightForWidth())
        self.LineEdit_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.LineEdit_7.setFont(font)
        self.LineEdit_7.setObjectName("LineEdit_7")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 100, 120, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.date_3 = QtWidgets.QDateEdit(self.centralwidget)
        self.date_3.setGeometry(QtCore.QRect(300, 180, 360, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_3.sizePolicy().hasHeightForWidth())
        self.date_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.date_3.setFont(font)
        self.date_3.setDateTime(QtCore.QDateTime(QtCore.QDate(1900, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_3.setObjectName("date_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 120, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 420, 311, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 260, 261, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.LineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit_9.setEnabled(True)
        
        self.LineEdit_9.setGeometry(QtCore.QRect(300, 20, 360, 35))
        #self.LineEdit_9.returnPressed.connect(self.return_pressed)
        
        #self.LineEdit_9.setLineWrapMode(QtWidgets.QLineEdit.NoWrap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineEdit_9.sizePolicy().hasHeightForWidth())
        self.LineEdit_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.LineEdit_9.setFont(font)
        self.LineEdit_9.setObjectName("LineEdit_9")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 340, 261, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.LineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit_10.setEnabled(True)
        self.LineEdit_10.setGeometry(QtCore.QRect(300, 340, 360, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineEdit_10.sizePolicy().hasHeightForWidth())
        self.LineEdit_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.LineEdit_10.setFont(font)
        self.LineEdit_10.setObjectName("LineEdit_10")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(300, 260, 91, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "-")
        for x in range(2,27):
            self.comboBox.addItem("")
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modification"))
        MainWindow.setWindowIcon(QtGui.QIcon('d.png'))
        self.label_11.setText(_translate("MainWindow", "Date"))
        self.label_10.setText(_translate("MainWindow", "Événement "))
        self.label_9.setText(_translate("MainWindow", "Lieu"))
        self.pushButton_5.setText(_translate("MainWindow", "Enregistrer"))
        self.label_13.setText(_translate("MainWindow", "Nombre de(s) Pérsonne(s)"))
        self.label_14.setText(_translate("MainWindow", "Nom(s) de(s) Pérsonne(s)"))
        self.comboBox.setItemText(1, _translate("MainWindow", "vide"))
        for x in range(1,27):
            self.comboBox.setItemText(x+1, _translate("MainWindow", str(x)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Modifier_ligne()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

