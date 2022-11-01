# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HP\Desktop\KBscan\Application_Photo_scan_BD\backup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 486)
        MainWindow.setStyleSheet("QWidget{\n"
"border : solid 10 px rgba(0,0,0);\n"
"background-color :#eee;\n"
"    }\n"
"\n"
"QTextEdit{\n"
"border-radius:10px;\n"
"border: 2px solid #000000;\n"
"background-color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QDateEdit{\n"
"border-radius:10px;\n"
"border: 2px solid #000000;\n"
"background-color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
" border:2px solid rgb(170, 170, 170);\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"background-color : #001f3f;\n"
"border: 2px solid #000000;\n"
"border-radius:10px;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(0, 0, 116);\n"
"}\n"
"\n"
"\n"
"QTextEdit:focus{\n"
" border:2px solid rgb(170, 170, 170);\n"
"}\n"
"QComboBox{\n"
"background : #55d1d3;\n"
"border: 2px solid #000000;\n"
"border-radius:10px;\n"
"background-color:rgb(255, 255, 255)\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setEnabled(True)
        self.textEdit_7.setGeometry(QtCore.QRect(300, 100, 360, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_7.sizePolicy().hasHeightForWidth())
        self.textEdit_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.textEdit_7.setFont(font)
        self.textEdit_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_7.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_7.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_7.setObjectName("textEdit_7")
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
        self.date_3.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 3, 1), QtCore.QTime(0, 0, 0)))
        self.date_3.setObjectName("date_3")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 260, 261, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
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
        self.pushButton_5.setGeometry(QtCore.QRect(150, 420, 311, 41))
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
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(300, 260, 81, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setIconSize(QtCore.QSize(20, 20))
        self.comboBox_3.setObjectName("comboBox_3")
        for x in range(20):
            self.comboBox_3.addItem("")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setEnabled(True)
        self.textEdit_8.setGeometry(QtCore.QRect(300, 340, 360, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_8.sizePolicy().hasHeightForWidth())
        self.textEdit_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.textEdit_8.setFont(font)
        self.textEdit_8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_8.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_8.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_8.setObjectName("textEdit_8")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 340, 261, 30))
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
        self.textEdit_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_9.setEnabled(True)
        self.textEdit_9.setGeometry(QtCore.QRect(300, 20, 360, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_9.sizePolicy().hasHeightForWidth())
        self.textEdit_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.textEdit_9.setFont(font)
        self.textEdit_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_9.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_9.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_9.setObjectName("textEdit_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_11.setText(_translate("MainWindow", "Date"))
        self.label_10.setText(_translate("MainWindow", "Événement "))
        self.label_12.setText(_translate("MainWindow", "Nombres de(s) Pérsonnes"))
        self.label_9.setText(_translate("MainWindow", "Lieu"))
        self.pushButton_5.setText(_translate("MainWindow", "Modifier"))
        for x in range(20):
            self.comboBox_3.setItemText(x, _translate("MainWindow", str(x+1)))
        self.label_13.setText(_translate("MainWindow", "Nom(s) de(s) Pérsonne(s)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

