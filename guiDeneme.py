from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLineEdit, QLabel
import sys
from turkishnlp import detector

obj = detector.TurkishNLP()
obj.create_word_set()

toplampuan = 0

baslangicKelimesi = "başarı"

kelime = ""

def puan_kazandir():

    bonus = 0

    global toplampuan
    kelimeUzunlugu = len(kelime)
    puan = kelimeUzunlugu * 4

    if(obj.is_vowel_harmonic(kelime)):
     print("%10 büyük ünlü uyumu bonusu ! ")
     bonus = bonus + 0.1

    if obj.is_turkish_origin(kelime):
     print("%20 Türkçe kökenli sözcük bonusu ! ")
     bonus = bonus + 0.2

    toplambonus = bonus + 1
    puan = puan * toplambonus
    toplampuan = toplampuan + puan

    print(kelime + " kelimesinden " + str(puan) + " kazandınız!\n")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "TurkishNLP Destekli Kelime Oyunu"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300


        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)

        self.setGeometry(self.left, self.top, self.width, self.height)
        hbox = QHBoxLayout()

        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit.returnPressed.connect(self.onPressed)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))

        self.label2 = QLabel(self)
        self.label2.setFont(QtGui.QFont("Sanserif", 15))

        self.buuBonus = QLabel(self)
        self.buuBonus.setFont(QtGui.QFont("Sanserif", 15))

        hbox.addWidget(self.label)
        hbox.addWidget(self.lineedit)
        hbox.addWidget(self.buuBonus)
        hbox.addWidget(self.label2)

        self.setLayout(hbox)
        self.show()


    def onPressed(self):
     kelime = self.lineedit.text()
     if obj.is_turkish(kelime):
        self.label.setText(self.lineedit.text())
        self.lineedit.clear()
        self.label2.setText("kelime turkce")
     if (obj.is_vowel_harmonic(kelime)):
        self.buuBonus.setText("%10 büyük ünlü uyumu bonusu ! ")

     else:
         self.lineedit.clear()
         self.label.clear()
         self.label2.clear()
         self.buuBonus.clear()




if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())