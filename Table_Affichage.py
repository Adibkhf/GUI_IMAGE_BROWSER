# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 14:42:28 2022

@author: HP
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HP\Desktop\KBscan\Application_Photo_scan_BD\Table_Affichage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtCore import Qt
import os.path



class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """    
    def __init__(self,qlabel_object):
        super().__init__()
        self.title = "zoom"
        self.qlabel_object = qlabel_object
        self.setWindowTitle(self.title)
    
        # Create widget
        self.label = QLabel(self)
        self.label.resize(600,600)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(self.qlabel_object,'jpg')
        pixmap.scaled(600, 600, Qt.KeepAspectRatio,Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)
        #label.setScaledContents(True)
        self.resize(600,600)
        
        
    def resizeEvent(self, event):
        pixmap1 = QtGui.QPixmap()
        pixmap1.loadFromData(self.qlabel_object,'jpg')
        self.pixmap = pixmap1.scaled(self.width(), self.height())
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.width(), self.height())
        
      
        
class Table_Afficher(object):

    
    def setupUi(self, MainWindow,cursor,sql_aff,nom_gui):
        self.nom_gui = nom_gui
        self.cursor = cursor
        self.sql_aff = sql_aff
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1540, 720)
        MainWindow.setStyleSheet("\n"
"\n"
"QHeaderView::section {\n"
"    \n"
"    padding: 6px;\n"
"    border-style: none;\n"
"    border-bottom: 2px solid black;\n"
"    border-right: 2px solid black;\n"
"    border-top: 2px solid black;\n"
"    border-left: 0px solid black;\n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"gridline-color: black;\n"
"border-left: 1px solid black;\n"
"\n"
"\n"
"}\n"
"QTableView::item {\n"
"border-right: 1px solid black;\n"
"border-bottom: 1px solid black;\n"
"\n"
"}\n"
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
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(MainWindow)
        #self.tableWidget.setGeometry(QtCore.QRect(0, 50, 1530, 600))
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(215)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        font2 = QtGui.QFont()
        font2.setFamily("Garamond")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        for x in range(7):
            self.tableWidget.horizontalHeaderItem(x).setFont(font2)
        font_tab = QtGui.QFont()
        font_tab.setFamily("Garamond")
        font_tab.setPointSize(10)
        self.tableWidget.setFont(font_tab)
       
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.clicked.connect(lambda: Selectionner_tout())
        #self.pushButton_2.setGeometry(QtCore.QRect(320, 660, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.clicked.connect(lambda: Telecharger())
        #self.pushButton_3.setGeometry(QtCore.QRect(620, 660, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(QtGui.QIcon("icon-file.png"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setIconSize(QtCore.QSize(28,24))
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        spacerItem = QtWidgets.QSpacerItem(718, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        #self.pushButton_5.setGeometry(QtCore.QRect(1040, 10, 41, 31))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid #000000;\n"
"border-radius:10px;\n"
"color:#fff;\n"
"}")
   
        self.pushButton_5.clicked.connect(lambda: Path())
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.textEdit.setGeometry(QtCore.QRect(1085, 10, 431, 31))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"border-radius:10px;\n"
"border: 2px solid #000000;\n"
"background-color:rgb(255, 255, 255)\n"
"}")
       
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        font_text = QtGui.QFont()
        font_text.setFamily("Garamond")
        font_text.setPointSize(12)
        self.textEdit.setFont(font_text)
        #----------------------------------------------Layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        
        
        self.horizontalLayout_5.addWidget(self.textEdit)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
    
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setContentsMargins(0,9,9,5)
        
    
        
        MainWindow.setCentralWidget(self.centralwidget)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        def convert_data(data, file_name,save_path):
            # Convert binary format to images
            # or files data(with given file_name)
            completeName = os.path.join(save_path, file_name+".jpg")         
            with open(completeName, 'wb') as file:
                try:
                    file.write(data)
                except:
                    pass
                
                
        def Telecharger():
            path = self.textEdit.toPlainText()
            #print(path)
            checked = []
            for x in range(len(res)):
                if self.tableWidget.item(x,0).checkState() == QtCore.Qt.Checked:
                    checked.append(self.tableWidget.item(x,0).text())
            if len(path)!= 0 and len(checked) != 0:
                l = self.tableWidget.rowCount()
                for x in range(l):
                    if self.tableWidget.item(x, 0).checkState() == Qt.CheckState.Checked:
                        convert_data(self.tab_x_y_images[x],self.tableWidget.item(x, 0).text(),path)
                    
            elif len(checked) == 0:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Erreur")
                msg.setText("Veuillez spécifier les images à telecharger")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setTextFormat(QtCore.Qt.RichText)
                msg.resize(msg.sizeHint())
                x = msg.exec_()
                
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Erreur")
                msg.setText("Veuillez spécifier l'emplacement des photos à telecharger")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setTextFormat(QtCore.Qt.RichText)
                msg.resize(msg.sizeHint())
                x = msg.exec_()

        def Path():
            #self.tableWidget.setRowCount(0)
            fname = QtWidgets.QFileDialog().getExistingDirectory()
            #print(fname)
            self.textEdit.setPlainText(fname)
        def Selectionner_tout():
            l = self.tableWidget.rowCount()
            if self.pushButton_2.text() == "Sélectionner Tout":
                for x in range(l): 
                    self.tableWidget.item(x, 0).setCheckState(Qt.CheckState.Checked)
                    self.pushButton_2.setText("Désélectionner Tout")
            elif self.pushButton_2.text() == "Désélectionner Tout":
                for x in range(l):
                    self.tableWidget.item(x, 0).setCheckState(Qt.CheckState.Unchecked)
                    self.pushButton_2.setText("Sélectionner Tout")
        def upper_name(tab):
            res = []
            for x in tab:
                n = []
                for y in x.split(' '):
                    n.append(y[0].upper()+y[1:])
                res.append(" ".join(n))
            return res
        def lower_name(tab):
            res = []
            for x in tab:
                n = []
                for y in x.split(' '):
                    n.append(y[0].lower()+y[1:])
                res.append(" ".join(n))
            return res 
        self.cursor.execute(self.sql_aff)
        res = []
        for x in self.cursor:
            res.append(x)
        res_fa = []
        if self.nom_gui == ["vide"]:
            res_fa = res
        elif len(self.nom_gui)>1 :
            tab_nom = lower_name(self.nom_gui)+ upper_name(self.nom_gui)
            #print(tab_nom)
            for x in res:
                if x[6] != None:
                    bd_nom=x[6].split(',')
                    if any(item in bd_nom for item in tab_nom) == True:
                        res_fa.append(x)
                else:
                    res_fa.append(x)
            res = res_fa
        self.tab_x_y_images = []            
        for row_number, row_data in enumerate(res):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data);
                if column_number == 0:
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole,column_data)
                    self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(item))
                elif(column_number == 1):
                    item = self.getImageLabel(column_data)
                    self.tab_x_y_images.append(column_data)
                    self.tableWidget.setCellWidget(row_number,column_number,item)
                elif item == "None":
                    item = QtWidgets.QTableWidgetItem("")
                    item.setFlags(item.flags() & ~Qt.ItemIsSelectable)
                    self.tableWidget.setItem(row_number,column_number,item)
                elif column_number == 4:
                    item = QtWidgets.QTableWidgetItem(item[8:10]+'-'+item[5:7]+'-'+item[0:4])
                    item.setFlags(item.flags() & ~Qt.ItemIsSelectable)
                    self.tableWidget.setItem(row_number,column_number,item)
                else:
                    item = QtWidgets.QTableWidgetItem(item)
                    item.setFlags(item.flags() & ~Qt.ItemIsSelectable)
                    self.tableWidget.setItem(row_number,column_number,item)
        self.tableWidget.verticalHeader().setDefaultSectionSize(160)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.selectionModel().selectionChanged.connect(self.on_selectionChanged)    
        
    
    def on_selectionChanged(self,selected,deselected):
        for x in selected.indexes():
            if x.column() == 0:
                if self.tableWidget.item(x.row(), 0).checkState()==QtCore.Qt.Unchecked:
                    self.tableWidget.item(x.row(), 0).setCheckState(Qt.CheckState.Checked)
                else:
                    self.tableWidget.item(x.row(), 0).setCheckState(Qt.CheckState.Unchecked)

                #self.tableWidget.item(x.row()+1, x.column()).setCheckState(Qt.CheckState.Checked)
            #print(x.row(),x.column())
            #print(self.tableWidget.item(x.row(), x.column()))
            #r = self.tableWidget.cellWidget(x.row(), x.column())
            #print(self.tab_x_y_images[x.row()])
            #r = self.tab_x_y_images[x.row()]
            #self.open_second_window(r)
            
            elif x.column()==1:
                self.w = AnotherWindow(self.tab_x_y_images[x.row()])
                self.w.show()
                self.tableWidget.clearSelection()

            
    def getImageLabel(self,image):
        imageLabel = QtWidgets.QLabel(self.centralwidget)
        imageLabel.setText("")
        imageLabel.setScaledContents(True)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image,'jpg')
        imageLabel.setPixmap(pixmap)
        return imageLabel
        
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        MainWindow.setWindowIcon(QtGui.QIcon('d.png'))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Image"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Lieu"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Événement"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Nombre de(s) Pérsonne(s)"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Nom(s) de(s) Pérsonne(s)"))
        self.pushButton_3.setText(_translate("MainWindow", "Telecharger"))
        self.pushButton_2.setText(_translate("MainWindow", "Sélectionner Tout"))


    
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Table_Afficher()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''
