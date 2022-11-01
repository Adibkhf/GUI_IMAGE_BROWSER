

from PyQt5 import QtCore, QtGui, QtWidgets
from Table_Affiche_Modifier import Table_Aff_Modif
from Table_Affichage import Table_Afficher
import mysql.connector
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
class CheckableComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        super(CheckableComboBox, self).__init__(parent)
        self.view().pressed.connect(self.handleItemPressed)
    #    self.view().pressed.connect(self.test_check)
        self._changed = False

        
    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            item.setCheckState(QtCore.Qt.Checked)
            
        #if self.itemChecked(0):
        #    item_tout = self.model().item(0, self.modelColumn())
        #    for x in range(1,self.count()):
        #        item = self.model().item(x, self.modelColumn())
        #        item = self.model().item(x, self.modelColumn())
        #        item.setCheckState(item_tout.checkState())
                    
        self._changed = True

    def hidePopup(self):
        if not self._changed:
            super(CheckableComboBox, self).hidePopup()
        self._changed = False

    def itemChecked(self, index):
        item = self.model().item(index, self.modelColumn())
        return item.checkState() == QtCore.Qt.Checked

    def setItemChecked(self, index, checked=True):
        item = self.model().item(index, self.modelColumn())
        if checked:
            item.setCheckState(QtCore.Qt.Checked)
        else:
            item.setCheckState(QtCore.Qt.Unchecked)
    def check_items(self):
        checkedItems = []
        for i in range(self.count()):
            if self.itemChecked(i):
                checkedItems.append(self.model().item(i, 0).text())
        return checkedItems
    
class Affichage(object):
        
    def Afficher_table(self,cursor,sql_aff,nom_gui):
        self.Ouvrir_table_window = QtWidgets.QMainWindow()
        self.ui_aff= Table_Afficher() 
        self.ui_aff.setupUi(self.Ouvrir_table_window,cursor,sql_aff,nom_gui)
        return self.Ouvrir_table_window
        #self.Ouvrir_table_window.show()
        
    def Ouvrir_table(self,cursor,sql_aff,nom_gui):
        self.Ouvrir_table_window = QtWidgets.QMainWindow()
        self.ui_modif = Table_Aff_Modif() 
        self.ui_modif.setupUi(self.Ouvrir_table_window,cursor,sql_aff,nom_gui)
        #self.Ouvrir_table_window.show()    
        return self.Ouvrir_table_window
        
    def setupUi(self, MainWindow,mydb):
        self.mydb = mydb
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(683, 545)
        MainWindow.setWindowIcon(QtGui.QIcon("d.png"))
        #MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

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
"QTextEdit{\n"
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
"combobox-popup: 0;\n"
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
        self.combobox_7 = CheckableComboBox(self.centralwidget)
        self.combobox_7.setGeometry(QtCore.QRect(300, 100, 360, 35))
        cursor = mydb.cursor(buffered=True)
        cursor.execute("SELECT Evenement FROM test.images;")
        res_evenement = []
        for x in cursor:
            if x[0] != None:
                for y in x[0].split(','):
                    res_evenement.append(y)
        res_evenement = list(set(res_evenement))
        res_evenement.sort()
        res_evenement = list(set(res_evenement))
        res_evenement = ["vide"] + res_evenement
        res_evenement = tuple(res_evenement)
        for index, element in enumerate(res_evenement):
            self.combobox_7.addItem(element)
            item = self.combobox_7.model().item(index, 0)
            item.setCheckState(QtCore.Qt.Unchecked)
        self.combobox_7.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
 
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.combobox_7.setFont(font)
 
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
        self.pushButton_5.clicked.connect(lambda: click_Aff())
        self.pushButton_5.pressed.connect(lambda: click_Aff())
        #self.pushButton_5.clicked.connect(lambda: self.Ouvrir_table(self.cursor))
        self.pushButton_5.setGeometry(QtCore.QRect(185, 420, 311, 41))
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

        self.combobox_9 = CheckableComboBox(self.centralwidget)
        self.combobox_9.setGeometry(QtCore.QRect(300, 20, 360, 35))
        cursor.execute("SELECT Lieu FROM test.images;")
        res_Lieu = []
        for x in cursor:
            if x[0] != None:
                for y in x[0].split(','):
                    res_Lieu.append(y)
        res_Lieu = list(set(res_Lieu))
        res_Lieu.sort()
        res_Lieu = list(set(res_Lieu))
        res_Lieu = ["vide"] + res_Lieu
        res_Lieu = tuple(res_Lieu)
        for index, element in enumerate(res_Lieu):
            self.combobox_9.addItem(element)
            item = self.combobox_9.model().item(index, 0)
            item.setCheckState(QtCore.Qt.Unchecked)
        self.combobox_9.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.combobox_9.setFont(font)
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
        
        
        #Combobox Nom des pérsonnes
        self.combobox_10 = CheckableComboBox(self.centralwidget)
        self.combobox_10.setGeometry(QtCore.QRect(300, 340, 360, 35))
        cursor.execute("SELECT Nom_des_personnes FROM test.images;")
        res_nom_personnes = []
        for x in cursor:
            if x[0] != None:
                for y in x[0].split(','):
                    res_nom_personnes.append(y)
        res_nom_personnes = list(set(res_nom_personnes))
        res_nom_personnes.sort()
        res_nom_personnes = list(set(res_nom_personnes))
        res_nom_personnes = ["vide"] + res_nom_personnes
        res_nom_personnes = tuple(res_nom_personnes)
        for index, element in enumerate(res_nom_personnes):
            self.combobox_10.addItem(element)
            item = self.combobox_10.model().item(index, 0)
            item.setCheckState(QtCore.Qt.Unchecked)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.combobox_10.setFont(font)
        self.combobox_10.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

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
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(5, 500, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("commandLinkButton")
        self.pushButton_6.clicked.connect(lambda: close_windows())
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(300, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "-")
        for x in range(31):
            self.comboBox_2.addItem("")
        
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(410, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(0, "-")
        for x in range(12):
            self.comboBox_3.addItem("")

        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(520, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(0, "-")
        for x in range(200):
            self.comboBox_4.addItem("")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(305, 210, 71, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(415, 210, 71, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(525, 210, 71, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(630, 180, 30, 35))
        self.pushButton_8.clicked.connect(lambda: label_plus())
        self.pushButton_8.setText('+')
        self.pushButton_8.setFont(font)
        
        self.label_12x = QtWidgets.QLabel(self.centralwidget)
        self.label_12x.setGeometry(QtCore.QRect(305, 700, 71, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12x.sizePolicy().hasHeightForWidth())
        self.label_12x.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12x.setFont(font)
        self.label_12x.setObjectName("label_12")
        self.label_15x = QtWidgets.QLabel(self.centralwidget)
        self.label_15x.setGeometry(QtCore.QRect(415, 700, 71, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15x.sizePolicy().hasHeightForWidth())
        self.label_15x.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15x.setFont(font)
        self.label_15x.setObjectName("label_15")
        self.label_16x = QtWidgets.QLabel(self.centralwidget)

        self.label_16x.setGeometry(QtCore.QRect(525, 700, 71, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16x.sizePolicy().hasHeightForWidth())
        self.label_16x.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16x.setFont(font)
        
        self.comboBox_2x = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2x.setGeometry(QtCore.QRect(300, 700, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2x.setFont(font)
        self.comboBox_2x.setObjectName("comboBox_2")
        self.comboBox_2x.addItem("")
        self.comboBox_2x.setItemText(0, "-")
        for x in range(31):
            self.comboBox_2x.addItem("")
        
        self.comboBox_3x = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3x.setGeometry(QtCore.QRect(410, 700, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3x.setFont(font)
        self.comboBox_3x.setObjectName("comboBox_3")
        self.comboBox_3x.addItem("")
        self.comboBox_3x.setItemText(0, "-")
        for x in range(12):
            self.comboBox_3x.addItem("")

        self.comboBox_4x = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4x.setGeometry(QtCore.QRect(520,700, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_4x.setFont(font)
        self.comboBox_4x.setObjectName("comboBox_4")
        self.comboBox_4x.addItem("")
        self.comboBox_4x.setItemText(0, "-")
        for x in range(200):
            self.comboBox_4x.addItem("")
        self.label_11x = QtWidgets.QLabel(self.centralwidget)
        self.label_11x.setGeometry(QtCore.QRect(20, 700, 171, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11x.sizePolicy().hasHeightForWidth())
        self.label_11x.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11x.setFont(font)
        self.comboBox_2.activated.connect(lambda: enable_combobox_2())
        self.comboBox_3.activated.connect(lambda: enable_combobox_3())
        self.comboBox_4.activated.connect(lambda: enable_combobox_4())
        
    
        self.comboBox_2x.setEnabled(False)
        self.comboBox_3x.setEnabled(False)
        self.comboBox_4x.setEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        def enable_combobox_2():
            if self.comboBox_2.currentText() != '-':
                self.comboBox_2x.setEnabled(True)
            else:
                self.comboBox_2x.setCurrentIndex(0)
                self.comboBox_2x.setEnabled(False)
        def enable_combobox_3():
            if self.comboBox_3.currentText() != '-':
                self.comboBox_3x.setEnabled(True)
            else:
                self.comboBox_3x.setCurrentIndex(0)
                self.comboBox_3x.setEnabled(False)
        def enable_combobox_4():
            if self.comboBox_4.currentText() != '-':
                self.comboBox_4x.setEnabled(True)
            else:
                self.comboBox_4x.setCurrentIndex(0)
                self.comboBox_4x.setEnabled(False)

                
                
        def label_plus():
            if self.pushButton_8.text()== "+":
                MainWindow.setFixedSize(683, 625)
                self.label.setGeometry(QtCore.QRect(-290, 0, 991, 691))
                self.label_13.setGeometry(QtCore.QRect(20, 340, 261, 30))
                self.label_14.setGeometry(QtCore.QRect(20, 420, 261, 30))
                self.combobox_10.setGeometry(QtCore.QRect(300, 420, 360, 35))
                self.comboBox.setGeometry(QtCore.QRect(300, 340, 91, 31))
                self.pushButton_5.setGeometry(QtCore.QRect(180, 500, 311, 41))
                self.pushButton_6.setGeometry(QtCore.QRect(5, 580, 101, 41))
                self.pushButton_8.setText("-")
                self.comboBox_2x.setGeometry(QtCore.QRect(300, 260, 81, 31))
                self.comboBox_3x.setGeometry(QtCore.QRect(410, 260, 81, 31))
                self.comboBox_4x.setGeometry(QtCore.QRect(520,260, 81, 31))
                self.label_12x.setGeometry(QtCore.QRect(305, 290, 71, 31))
                self.label_15x.setGeometry(QtCore.QRect(415, 290, 71, 31))
                self.label_16x.setGeometry(QtCore.QRect(525, 290, 71, 31))
                self.label_11x.setGeometry(QtCore.QRect(20, 260, 171, 31))
                self.label_11.setText("De")
            elif self.pushButton_8.text()== "-":
                MainWindow.setFixedSize(683, 545)
                self.label.setGeometry(QtCore.QRect(-290, -100, 991, 691))
                self.pushButton_8.setText("+")
                self.label_13.setGeometry(QtCore.QRect(20, 260, 261, 30))
                self.label_14.setGeometry(QtCore.QRect(20, 340, 261, 30))
                self.comboBox.setGeometry(QtCore.QRect(300, 260, 91, 31))
                self.combobox_10.setGeometry(QtCore.QRect(300, 340, 360, 35))
                self.pushButton_5.setGeometry(QtCore.QRect(185, 420, 311, 41))
                self.pushButton_6.setGeometry(QtCore.QRect(5, 500, 101, 41))
                self.comboBox_2x.setGeometry(QtCore.QRect(300, 700, 81, 31))
                self.comboBox_3x.setGeometry(QtCore.QRect(410, 700, 81, 31))
                self.comboBox_4x.setGeometry(QtCore.QRect(520,700, 81, 31))
                self.label_12x.setGeometry(QtCore.QRect(305, 700, 71, 31))
                self.label_15x.setGeometry(QtCore.QRect(415, 700, 71, 31))
                self.label_16x.setGeometry(QtCore.QRect(525, 700, 71, 31))
                self.label_11x.setGeometry(QtCore.QRect(20, 700, 171, 31))
                self.label_11.setText("Date")
        def closeEvent(self, event):
            for window in QApplication.topLevelWidgets():
                window.close()
        def close_windows():
            try:
                self.ww.close()
            except:
                pass
        def click_Aff():
            
            dictio_column_Affiche = {}
            #dictio_column_Affiche['Lieu'] =  self.textEdit_9.toPlainText().split(",")
            dictio_column_Affiche['Lieu'] =  self.combobox_9.check_items()
           
            #dictio_column_Affiche['Evenement'] = self.textEdit_7.toPlainText().strip().split(",")
            dictio_column_Affiche['Evenement'] =  self.combobox_7.check_items()
   
            jour = self.comboBox_2.currentText()
            mois = self.comboBox_3.currentText()  
            année = self.comboBox_4.currentText()
            
            jourx = self.comboBox_2x.currentText()
            moisx = self.comboBox_3x.currentText()  
            annéex = self.comboBox_4x.currentText()       
            
            dictio_column_Affiche['Date_eve'] = (jour,mois,année)
            #dictio_column_Affiche['Date_Jusqua'] = (jourx,moisx,annéex)
            tab_date = []
            dict_date = {}
            for a,b in zip(["DAY","MONTH","YEAR"],[jour,mois,année]):
                dict_date[a] = b
            
            for a in [jour,mois,année]:
                if a == "-":
                    tab_date.append(0)
                else:
                    tab_date.append(1)
                    
            tab_datex = []
            dict_datex = {}
            for ax,bx in zip(["DAY","MONTH","YEAR"],[jourx,moisx,annéex]):
                dict_datex[ax] = bx
            
            for ax in [jourx,moisx,annéex]:
                if ax == "-":
                    tab_datex.append(0)
                else:
                    tab_datex.append(1)
                 
            
            
            dictio_column_Affiche['Nombre_de_personne'] = self.comboBox.currentText()

            
            #dictio_column_Affiche['Nom_des_personnes'] = self.textEdit_10.toPlainText().strip().split(",")
            dictio_column_Affiche['Nom_des_personnes'] =  self.combobox_10.check_items()
            
            #print(dictio_column_Affiche)
            if "-" in dictio_column_Affiche['Nom_des_personnes']:
                dictio_column_Affiche['Nombre_de_personne'].remove('-')
            #print(dictio_column_Affiche)
            dict_bin = {}
            for x in dictio_column_Affiche:
                if x == 'Date_eve':
                    dict_bin[x] = int(any(tab_date))
                #elif x == "Date_Jusqua":
                #    dict_bin[x] = int(any(tab_datex))
                elif dictio_column_Affiche[x]==[] or dictio_column_Affiche[x]=='-':
                    dict_bin[x]=0
                else:
                    dict_bin[x]=1
            #print(dict_bin)
            def sql_gener(xa):
                res = "("
                if xa == 'Nom_des_personnes':
                    for x in dictio_column_Affiche[xa]:
                        if x == 'vide':
                            r = "Nombre_de_personne>length(Nom_des_personnes)-length(replace(Nom_des_personnes,',',''))+1 or Nom_des_personnes is NULL or "
                            res += r
                        else:
                            r = xa+" like '%"+x.strip()+"%' or "
                            res += r
                    res = res[:-4]+")"
                elif xa == "Date_eve":
                    if int(any(tab_datex))== 0:
                        for x in dict_date:
                            if dict_date[x]!="-":
                                r = x+"("+xa+")"+"="+dict_date[x]+" and "
                                res+= r
                        res = res[:-5]+")"
                    else:
                        for x in dict_datex:
                            if dict_date[x]!="-" and dict_datex[x]=='-':
                                r = x+"("+xa+")"+"="+dict_date[x]+" and "
                                res+= r
                            if dict_datex[x]!="-" and dict_date[x]!='-':
                                r = x+"("+xa+")"+" between "+dict_date[x]+ " and "+dict_datex[x]+" and "
                                res += r
                        res = res[:-5]+")"
                elif xa == 'Nombre_de_personne':
                    if dictio_column_Affiche[xa] == 'vide':
                        r = xa+" IS NULL or "+xa+"='')"  
                        res+=r
                    else:
                        r = xa+"="+str(dictio_column_Affiche[xa])+")"  
                        res+=r
                else:
                    for x in dictio_column_Affiche[xa]:
                        if x == 'vide':
                            r = xa+" IS NULL or "+xa+"='' or "
                            res += r
                        else:
                            r = xa+"='"+x.strip()+"' or "
                            res += r
                    res = res[:-4]+")"
                
                return res
            sql_affiche = ''

            if sum(dict_bin.values())==0:
                sql_affiche = "SELECT * FROM images;"
                print(sql_affiche)
                #self.cursor.execute("SELECT * FROM images;")
            else:
                S = "SELECT * FROM images WHERE "
                for x in ['Lieu','Evenement','Nom_des_personnes','Date_eve','Nombre_de_personne']:
                    if dict_bin[x] == 1:
                        S+= sql_gener(x)+" AND "
                S = S[:-5]+";"    
                sql_affiche = S
                print(sql_affiche)
                print(dict_bin)
                #self.cursor.execute(S)
            self.Ouvrir_table_window = QtWidgets.QMainWindow()
            
            cursor = mydb.cursor(buffered=True)
            cursor.execute("SHOW GRANTS FOR CURRENT_USER;")
            nom_gui = dictio_column_Affiche['Nom_des_personnes']
            for x in cursor:
               res = x
            self.ww = None
            print('UPDATE' in res[0])
            if 'UPDATE' in res[0]:
                #self.ui_modif = Table_Aff_Modif() 
                #self.ui_modif.setupUi(self.Ouvrir_table_window,cursor,sql_affiche)
                self.ww = self.Ouvrir_table(cursor,sql_affiche,nom_gui)
                self.ww.show()
            else:
                self.ww = self.Afficher_table(cursor,sql_affiche,nom_gui) 
                self.ww.show()
           
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
       

        self.label_11.setText(_translate("MainWindow", "Date"))
        self.label_11x.setText(_translate("MainWindow", "Jusqu'à"))
        self.label_10.setText(_translate("MainWindow", "Événement "))
        self.label_9.setText(_translate("MainWindow", "Lieu"))
        self.pushButton_5.setText(_translate("MainWindow", "Afficher"))
        self.label_13.setText(_translate("MainWindow", "Nombre de(s) Pérsonne(s)"))
        self.label_14.setText(_translate("MainWindow", "Nom(s) de(s) Pérsonne(s)"))
        self.comboBox.setItemText(1, _translate("MainWindow", "vide"))
        self.label_12.setText(_translate("MainWindow", "Jour"))
        self.label_15.setText(_translate("MainWindow", "Mois"))
        self.label_16.setText(_translate("MainWindow", "Année"))
        
        self.label_12x.setText(_translate("MainWindow", "Jour"))
        self.label_15x.setText(_translate("MainWindow", "Mois"))
        self.label_16x.setText(_translate("MainWindow", "Année"))
        for x in range(1,27):
            self.comboBox.setItemText(x+1, _translate("MainWindow", str(x)))
        for x in range(31):
            if x<9:
                self.comboBox_2.setItemText(x+1, _translate("MainWindow", "0"+str(x+1)))
                self.comboBox_2x.setItemText(x+1, _translate("MainWindow", "0"+str(x+1)))
            else:
                self.comboBox_2.setItemText(x+1, _translate("MainWindow", str(x+1)))
                self.comboBox_2x.setItemText(x+1, _translate("MainWindow", str(x+1)))
        for x in range(12):
            if x<9:
                self.comboBox_3.setItemText(x+1, _translate("MainWindow", "0"+str(x+1)))
                self.comboBox_3x.setItemText(x+1, _translate("MainWindow", "0"+str(x+1)))
            else:
                self.comboBox_3.setItemText(x+1, _translate("MainWindow", str(x+1)))
                self.comboBox_3x.setItemText(x+1, _translate("MainWindow", str(x+1)))
        for x in range(200):
            self.comboBox_4.setItemText(x+1, _translate("MainWindow", str(2030-x)))
            self.comboBox_4x.setItemText(x+1, _translate("MainWindow", str(2030-x)))       

         
            
        self.pushButton_6.setText(_translate("MainWindow", "Déconnexion"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Affichage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



