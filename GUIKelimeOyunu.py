
# GUI Kelime Oyunu

# PyQT5, turkishnlp kurulumu gerektirir ->> pip install pytq5 , pip install turkishnlp

# 1 kere çalıştırdıktan sonra obj.download() satırını siliniz

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLineEdit, QLabel, QVBoxLayout, QMainWindow, QPushButton
import sys
from turkishnlp import detector
import pipeline_caller

caller = pipeline_caller.PipelineCaller()
token = "0JARhJpaEG7vERnZ5P2SctdrhHmrMivs"

obj = detector.TurkishNLP()

#Bir kere çalıştırdıktan sonra siliniz
obj.download()
#Bir kere çalıştırdıktan sonra siliniz

obj.create_word_set()

toplampuan = 0

baslangicKelimesi = "başarı"

kelime = ""

kelimeler = []

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
        self.pushButton = QPushButton("Başla", self)
        self.label = QLabel(self)

        self.label.setAlignment(Qt.AlignCenter)

        vBox = QVBoxLayout()
        vBox.addWidget(self.label)
        vBox.addWidget(self.pushButton)
        self.setLayout(vBox)

        self.label.setFont(QtGui.QFont("Sanserif", 15))
        self.label.setText(

            "TurkishNLP Destekli Kelime Bulma Oyununa\nHoşgeldiniz!\n\n"
            "Bu oyun verilen kelimenin son harfi ile başlayan bir\n"
            "kelime yazan kullanıcıya puan kazandırmayı hedefler.\n\n"
            "\n"
            "->> Normalization, isturkish, is_vowel_harmonic, is_turkish_origin\n"
            "fonksiyonları kullanılmıştır.\n\n"
            "Başlamak İçin Tuşa Basın\n")

        self.pushButton.clicked.connect(self.window2)  # <===
        self.main_window()

    def main_window(self):
        self.setWindowTitle(self.title)
        self.show()

    def window2(self):  # <===
        self.w = Window2()
        self.w.show()
        self.hide()


class Window2(QWidget):

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
        vBox = QVBoxLayout()

        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit.returnPressed.connect(self.onPressed)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        self.label.setAlignment(Qt.AlignCenter)

        self.buuBonus = QLabel(self)
        self.buuBonus.setFont(QtGui.QFont("Sanserif", 15))
        self.buuBonus.setAlignment(Qt.AlignCenter)

        self.tksBonus = QLabel(self)
        self.tksBonus.setFont(QtGui.QFont("Sanserif", 15))
        self.tksBonus.setAlignment(Qt.AlignCenter)

        self.puanLabel = QLabel(self)
        self.puanLabel.setFont(QtGui.QFont("Sanserif", 15))
        self.puanLabel.setAlignment(Qt.AlignCenter)

        self.anlıkPuan = QLabel(self)
        self.anlıkPuan.setFont(QtGui.QFont("Sanserif", 15))
        self.anlıkPuan.setAlignment(Qt.AlignCenter)

        vBox.addWidget(self.label)
        vBox.addWidget(self.lineedit)
        vBox.addWidget(self.buuBonus)
        vBox.addWidget(self.tksBonus)
        vBox.addWidget(self.anlıkPuan)
        vBox.addWidget(self.puanLabel)

        self.setLayout(vBox)
        self.puanLabel.setText("Toplam Puanınız : " + str(toplampuan))
        self.label.setText("Kelime : " + str(baslangicKelimesi))
        self.show()

    def onPressed(self):
        global toplampuan
        global baslangicKelimesi
        bonus = 0

        kelime = self.lineedit.text()
        if kelime.startswith(baslangicKelimesi[-1]):
            if kelime not in kelimeler:
                # itü pipelineı cevap vermiyor
                # if caller.call("isturkish", kelime, token) == "true":
                if obj.is_turkish(kelime):
                    kelimeler.append(kelime)
                    baslangicKelimesi = kelime
                    self.label.setText("Kelime : " + self.lineedit.text())
                    self.lineedit.clear()

                    kelimeUzunlugu = len(kelime)
                    puan = kelimeUzunlugu * 4
                    print(puan)

                    if (obj.is_vowel_harmonic(kelime)):
                        self.buuBonus.setText("%10 büyük ünlü uyumu bonusu ! ")
                        bonus = bonus + 0.1
                    if (obj.is_vowel_harmonic(kelime)) == 0:
                        self.buuBonus.clear()
                    if obj.is_turkish_origin(kelime):
                        self.tksBonus.setText("%20 türkçe köken uyumlu sözcük uyumu bonusu ! ")
                        bonus = bonus + 0.2
                    if obj.is_turkish_origin(kelime) == 0:
                        self.tksBonus.clear()

                    toplambonus = bonus + 1
                    puan = puan * toplambonus
                    toplampuan = toplampuan + puan
                    self.puanLabel.setText("Toplam Puanınız : " + str(toplampuan))
                    self.anlıkPuan.setText(kelime + " kelimesinden : " + str(puan) + " puan kazandınız")
                    print(toplampuan)

                else:

                    lwords = obj.list_words(kelime)
                    corrected_words = obj.auto_correct(lwords)
                    corrected_string = " ".join(corrected_words)

                    kelimeUzunlugu = len(corrected_string)
                    puan = kelimeUzunlugu * 4

                    # itü pipeline çalışmıyor
                    # if caller.call("isturkish", corrected_string, token) == "true":
                    if obj.is_turkish(corrected_string):
                        if corrected_string not in kelimeler:
                            kelimeler.append(corrected_string)
                            baslangicKelimesi = corrected_string
                            self.label.setText(
                                self.lineedit.text() + " kelimesi " + corrected_string + " olarak değiştrildi! Son harf -> " +
                                corrected_string[-1])
                            self.anlıkPuan.setText(
                                corrected_string + " kelimesinden : " + str(puan) + " puan kazandınız")
                            self.lineedit.clear()

                            if (obj.is_vowel_harmonic(corrected_string)):
                                self.buuBonus.setText("%10 büyük ünlü uyumu bonusu ! ")
                                bonus = bonus + 0.1
                            if (obj.is_vowel_harmonic(corrected_string)) == 0:
                                self.buuBonus.clear()
                            if obj.is_turkish_origin(corrected_string):
                                self.tksBonus.setText("%20 türkçe köken uyumlu sözcük uyumu bonusu ! ")
                                bonus = bonus + 0.2
                            if obj.is_turkish_origin(corrected_string) == 0:
                                self.tksBonus.clear()

                            toplambonus = bonus + 1
                            puan = puan * toplambonus
                            toplampuan = toplampuan + puan
                            print(toplampuan)
                            self.puanLabel.setText("Toplam Puanınız : " + str(toplampuan))
                        else:
                            self.lineedit.clear()
                            self.label.setText(
                                "Bu kelime daha önce kullanıldı. Son harf - " + baslangicKelimesi[-1] + " - devam et!")
                            self.anlıkPuan.clear()
                            self.buuBonus.clear()
                            self.tksBonus.clear()
                    else:
                        self.lineedit.clear()
                        self.label.setText(
                            "kelime türkçe değil! Devam et! Kelimenin ilk harfi - " + baslangicKelimesi[
                                -1] + " - olmalı!")
                        self.anlıkPuan.clear()
                        self.buuBonus.clear()
                        self.tksBonus.clear()
            else:
                self.lineedit.clear()
                self.label.setText(
                    "Bu kelime daha önce kullanıldı. Son harf - " + baslangicKelimesi[-1] + " - devam et!")
                self.anlıkPuan.clear()
                self.buuBonus.clear()
                self.tksBonus.clear()
        else:
            self.lineedit.clear()
            self.label.setText("Kelime eşleşmiyor! Kelimenin ilk harfi - " + baslangicKelimesi[-1] + " - olmalı!")
            self.anlıkPuan.clear()
            self.buuBonus.clear()
            self.tksBonus.clear()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
