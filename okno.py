from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import json


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.zadavaciOkno = QtWidgets.QLineEdit(self.centralwidget)
        self.zadavaciOkno.setFont(font)
        self.zadavaciOkno.setGeometry(QtCore.QRect(20, 50, 300, 35))
        self.zadavaciOkno.setObjectName("zadavaciOkno")
        self.zadavaciOkno.adjustSize()
        self.btHledat = QtWidgets.QPushButton(self.centralwidget)
        self.btHledat.setGeometry(QtCore.QRect(350, 50, 100, 35))
        self.btHledat.setObjectName("btHledat")
        self.labelLogin = QtWidgets.QLabel(self.centralwidget)
        self.labelLogin.setGeometry(QtCore.QRect(20, 110, 90, 24))
        self.labelLogin.setFont(font)
        self.labelLogin.setObjectName("labelLogin")
        self.labelHeslo = QtWidgets.QLabel(self.centralwidget)
        self.labelHeslo.setGeometry(QtCore.QRect(20, 150, 90, 24))
        self.labelHeslo.setFont(font)
        self.labelHeslo.setObjectName("labelHeslo")
        self.vypisHeslo = QtWidgets.QLabel(self.centralwidget)
        self.vypisHeslo.setGeometry(QtCore.QRect(150, 150, 150, 24))
        self.vypisHeslo.setFont(font)
        self.vypisHeslo.setObjectName("vypisHeslo")
        self.vypisLogin = QtWidgets.QLabel(self.centralwidget)
        self.vypisLogin.setGeometry(QtCore.QRect(150, 110, 150, 24))
        self.vypisLogin.setFont(font)
        self.vypisLogin.setObjectName("vypisLogin")
        self.labelPoznamka = QtWidgets.QLabel(self.centralwidget)
        self.labelPoznamka.setGeometry(QtCore.QRect(20, 190, 200, 24))
        self.labelPoznamka.setFont(font)
        self.labelPoznamka.setObjectName("labelPoznamka")
        self.vypisPoznamka = QtWidgets.QLabel(self.centralwidget)
        self.vypisPoznamka.setGeometry(QtCore.QRect(20, 230, 450, 300))
        self.vypisPoznamka.setFont(font)
        self.vypisPoznamka.setFrameShape(QtWidgets.QFrame.Box)
        self.vypisPoznamka.setTextFormat(QtCore.Qt.PlainText)
        self.vypisPoznamka.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.vypisPoznamka.setObjectName("vypisPoznamka")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setFont(font)
        self.label_7.setGeometry(QtCore.QRect(30, 5, 200, 24))
        self.label_7.setObjectName("label_7")
        self.label_7.setText("Správce hesel")
        self.label_7.adjustSize()
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 550, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 550, 100, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 550, 100, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.labelLogin.setText("Login:")
        self.labelHeslo.setText("Heslo:")
        self.vypisHeslo.setText("")
        self.vypisLogin.setText("")
        self.labelPoznamka.setText("Poznámka:")
        self.vypisPoznamka.setText("")
        self.pushButton.setText("Přidat")
        self.pushButton_2.setText("Změnit")
        self.pushButton_3.setText("Smazat")
        self.btHledat.setText("Hledat")
        
        self.labelLogin.adjustSize()
        self.labelHeslo.adjustSize()
        self.labelPoznamka.adjustSize()
        self.vypisPoznamka.setStyleSheet("padding :1px")
        self.pushButton.adjustSize()
        self.pushButton_2.adjustSize()
        self.pushButton_3.adjustSize()
        self.btHledat.adjustSize()

        self.btHledat.clicked.connect(self.search)
        self.pushButton.clicked.connect(self.kliknutoPridat)
        self.pushButton_2.clicked.connect(self.kliknutoZmenit)
        self.pushButton_3.clicked.connect(self.kliknutoSmazat)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def kliknutoPridat(self):
        self.dialog = pridat()
        self.dialog.show()
    
    def kliknutoZmenit(self):
        self.dialog = zmenit()
        self.dialog.show()
    
    def kliknutoSmazat(self):
        self.dialog = smazat()
        self.dialog.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    
    def importDB():
        with open ('data.json', 'r') as file:
            database = json.load(file)
            return database


    def search(self):
        DBpasswords = []
        DBpasswords = self.importDB()
        input = self.zadavaciOkno.text().lower()
        for i in range(0, len(self.DBpasswords)):
            prvek = self.DBpasswords[i]['alias']
            for j in prvek:
                if (j.find(input)) >= 0:
                    self.vypisHeslo.setText(self.DBpasswords[i]['password'])
                    self.vypisLogin.setText(self.DBpasswords[i]['name'])
                    self.vypisHeslo.adjustSize()
                    self.vypisLogin.adjustSize()
                    self.vypisPoznamka.setText(self.DBpasswords[i]['note'])

class pridat(QMainWindow):
    def __init__(self):
        super(pridat, self).__init__()
        self.setGeometry(100,100,500,650)
        self.setWindowTitle("Moje první okno")
        self.initUI()
    
    def initUI(self):
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font2 = QtGui.QFont()
        font2.setFamily("Calibri")
        font2.setPointSize(12)
        self.popisek = QtWidgets.QLabel(self)
        self.popisek.setText("Přidání do databáze")
        self.popisek.move(10,10)
        self.popisek.setFont(font)
        self.popisek.adjustSize()
        self.popisek = QtWidgets.QLabel(self)
        self.popisek.setText("Přidání do databáze")
        self.popisek.move(10,10)
        self.popisek.setFont(font)
        self.popisek.adjustSize()
        self.labelLogin = QtWidgets.QLabel(self)
        self.labelLogin.setGeometry(20, 60, 90, 24)
        self.labelLogin.setFont(font)
        self.labelLogin.setObjectName("labelLogin")
        self.labelLogin.setText("Login: ")
        self.labelLogin.adjustSize()
        self.labelHeslo = QtWidgets.QLabel(self)
        self.labelHeslo.setGeometry(20, 110, 90, 24)
        self.labelHeslo.setFont(font)
        self.labelHeslo.setObjectName("labelHeslo")
        self.labelHeslo.setText("Heslo: ")
        self.labelHeslo.adjustSize()
        self.labelAlias = QtWidgets.QLabel(self)
        self.labelAlias.setGeometry(20, 160, 90, 24)
        self.labelAlias.setFont(font)
        self.labelAlias.setObjectName("labelHeslo")
        self.labelAlias.setText("Alias: ")
        self.labelAlias.adjustSize()
        self.labelPozn = QtWidgets.QLabel(self)
        self.labelPozn.setGeometry(20, 360, 90, 24)
        self.labelPozn.setFont(font)
        self.labelPozn.setObjectName("labelHeslo")
        self.labelPozn.setText("Pozn.: ")
        self.labelPozn.adjustSize()
        self.zadavaciOkno = QtWidgets.QLineEdit(self)
        self.zadavaciOkno.setFont(font)
        self.zadavaciOkno.setGeometry(150, 60, 150, 24)
        self.zadavaciOkno.setObjectName("zadavaciOkno")
        self.zadavaciOkno.adjustSize()
        self.zadavaciOkno2 = QtWidgets.QLineEdit(self)
        self.zadavaciOkno2.setFont(font)
        self.zadavaciOkno2.setGeometry(150, 110, 150, 24)
        self.zadavaciOkno2.setObjectName("zadavaciOkno2")
        self.zadavaciOkno2.adjustSize()
        self.zadavaciOkno3 = QtWidgets.QTextEdit(self)
        self.zadavaciOkno3.setFont(font2)
        self.zadavaciOkno3.setGeometry(150, 160, 150, 10)
        self.zadavaciOkno3.setObjectName("zadavaciOkno3")
        self.zadavaciOkno3.adjustSize()
        self.zadavaciOkno4 = QtWidgets.QTextEdit(self)
        self.zadavaciOkno4.setFont(font2)
        self.zadavaciOkno4.setGeometry(150, 360, 150, 10)
        self.zadavaciOkno4.setObjectName("zadavaciOkno4")
        self.zadavaciOkno4.adjustSize()
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(150, 570, 150, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setText("Přidat údaje")
        self.pushButton.adjustSize()
        self.pushButton.clicked.connect(self.kliknutoPridat)

    def importDB():
        with open ('data.json', 'r') as file:
            database = json.load(file)
            return database

    DBpasswords = []
    DBpasswords = importDB()

    def kliknutoPridat(self):
        login = self.zadavaciOkno.text()
        heslo = self.zadavaciOkno2.text()
        alias = self.zadavaciOkno3.text()
        poznamka = self.zadavaciOkno4.text()
        self.addNewItem(login,heslo,alias, poznamka)
        self.saveDB()

    def addNewItem(self, name, password, alias, note):
        self.new_data = {}
        self.new_data["name"] = name
        self.new_data["password"] = password
        self.new_data["alias"] = alias
        self.new_data["note"] = note
        self.DBpasswords.append(self.new_data)

    def saveDB(self):
        with open ('data.json', 'w') as file:
            json.dump(self.DBpasswords, file)

class zmenit(QMainWindow):
    def __init__(self):
        super(zmenit, self).__init__()
        self.setGeometry(100,100,500,650)
        self.setWindowTitle("Moje první okno")
        self.initUI()
    
    def initUI(self):
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font2 = QtGui.QFont()
        font2.setFamily("Calibri")
        font2.setPointSize(12)
        self.popisek = QtWidgets.QLabel(self)
        self.popisek.setText("Přidání do databáze")
        self.popisek.move(10,10)
        self.popisek.setFont(font)
        self.popisek.adjustSize()
        self.labelLogin = QtWidgets.QLabel(self)
        self.labelLogin.setGeometry(20, 60, 90, 24)
        self.labelLogin.setFont(font)
        self.labelLogin.setObjectName("labelLogin")
        self.labelLogin.setText("Login: ")
        self.labelLogin.adjustSize()
        self.labelHeslo = QtWidgets.QLabel(self)
        self.labelHeslo.setGeometry(20, 110, 90, 24)
        self.labelHeslo.setFont(font)
        self.labelHeslo.setObjectName("labelHeslo")
        self.labelHeslo.setText("Heslo: ")
        self.labelHeslo.adjustSize()
        self.labelAlias = QtWidgets.QLabel(self)
        self.labelAlias.setGeometry(20, 160, 90, 24)
        self.labelAlias.setFont(font)
        self.labelAlias.setObjectName("labelHeslo")
        self.labelAlias.setText("Alias: ")
        self.labelAlias.adjustSize()
        self.labelPozn = QtWidgets.QLabel(self)
        self.labelPozn.setGeometry(20, 360, 90, 24)
        self.labelPozn.setFont(font)
        self.labelPozn.setObjectName("labelHeslo")
        self.labelPozn.setText("Pozn.: ")
        self.labelPozn.adjustSize()
        self.zadavaciOkno = QtWidgets.QLineEdit(self)
        self.zadavaciOkno.setFont(font)
        self.zadavaciOkno.setGeometry(150, 60, 150, 24)
        self.zadavaciOkno.setObjectName("zadavaciOkno")
        self.zadavaciOkno.adjustSize()
        self.zadavaciOkno2 = QtWidgets.QLineEdit(self)
        self.zadavaciOkno2.setFont(font)
        self.zadavaciOkno2.setGeometry(150, 110, 150, 24)
        self.zadavaciOkno2.setObjectName("zadavaciOkno2")
        self.zadavaciOkno2.adjustSize()
        self.zadavaciOkno3 = QtWidgets.QTextEdit(self)
        self.zadavaciOkno3.setFont(font2)
        self.zadavaciOkno3.setGeometry(150, 160, 150, 10)
        self.zadavaciOkno3.setObjectName("zadavaciOkno3")
        self.zadavaciOkno3.adjustSize()
        self.zadavaciOkno4 = QtWidgets.QTextEdit(self)
        self.zadavaciOkno4.setFont(font2)
        self.zadavaciOkno4.setGeometry(150, 360, 150, 10)
        self.zadavaciOkno4.setObjectName("zadavaciOkno4")
        self.zadavaciOkno4.adjustSize()
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(150, 570, 150, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setText("Přidat údaje")
        self.pushButton.adjustSize()
        self.pushButton.clicked.connect(self.kliknutoPridat)

    def importDB():
        with open ('data.json', 'r') as file:
            database = json.load(file)
            return database

    DBpasswords = []
    DBpasswords = importDB()

    def kliknutoPridat(self):
        login = self.zadavaciOkno.text()
        heslo = self.zadavaciOkno2.text()
        alias = self.zadavaciOkno3.text()
        poznamka = self.zadavaciOkno4.text()
        self.addNewItem(login,heslo,alias, poznamka)
        self.saveDB()

    def addNewItem(self, name, password, alias, note):
        self.new_data = {}
        self.new_data["name"] = name
        self.new_data["password"] = password
        self.new_data["alias"] = alias
        self.new_data["note"] = note
        self.DBpasswords.append(self.new_data)

    def saveDB(self):
        with open ('data.json', 'w') as file:
            json.dump(self.DBpasswords, file)

class smazat(QMainWindow):
    def __init__(self):
        super(smazat, self).__init__()
        self.setGeometry(100,100,500,400)
        self.setWindowTitle("Moje první okno")
        self.initUI()
    
    def initUI(self):
        self.popisek = QtWidgets.QLabel(self)
        self.popisek.setText("Ahoj Jakube!")
        self.popisek.setStyleSheet("border: 1px solid black;")
        self.popisek.move(100,100)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

sys.exit(app.exec_())
