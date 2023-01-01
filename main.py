from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class mojeOkno(QMainWindow):
    def __init__(self):
        super(mojeOkno, self).__init__()
        self.setGeometry(100,100,500,400)
        self.setWindowTitle("Moje první okno")
        self.initUI()
    
    def initUI(self):
        self.popisek = QtWidgets.QLabel(self)
        self.popisek.setText("Ahoj Jakube!")
        self.popisek.setStyleSheet("border: 1px solid black;")
        self.popisek.move(100,100)

        self.tlacitko = QtWidgets.QPushButton(self)
        self.tlacitko.setText("Potvrdit")
        self.tlacitko.clicked.connect(self.kliknuto)
        
        
    def kliknuto(self):
        self.popisek.setText("Bylo na něj kliknuto!!!")
        self.update()

    def update(self):
        self.popisek.adjustSize()

def okno():
    aplikace = QtWidgets.QApplication(sys.argv)
    formular = mojeOkno()
    formular.show()
    sys.exit(aplikace.exec_())

okno()




