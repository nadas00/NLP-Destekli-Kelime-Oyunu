from turkishnlp import detector

obj = detector.TurkishNLP()
obj.create_word_set()

my_array = []
i = 0

baslangicKelimesi = "başarı"


def puan_kazandir():
    kelimeUzunlugu = len(kelime)
    puan = kelimeUzunlugu * 4

    if(obj.is_vowel_harmonic(kelime)):
        puan = puan * 1.25
        print("%25 büyük ünlü uyumu bonusu ! " +kelime + " kelimesinden " + str(puan) + " kazandınız!")
    else:
        print(kelime + " kelimesinden " + str(puan) + " kazandınız!")




while i < 5:
    kelime = input()

    if kelime.startswith(baslangicKelimesi[-1]):

        if obj.is_turkish(kelime):
            puan_kazandir()
            baslangicKelimesi = kelime

        else:
            lwords = obj.list_words(kelime)
            corrected_words = obj.auto_correct(lwords)
            corrected_string = " ".join(corrected_words)
            if obj.is_turkish(corrected_string):
                print(
                    '"' + kelime + '"' + " Türkçe bir kelime değil " + '"' + corrected_string + '"' + " demek istemiş olabilirsiniz")
                print("-->Son Harf : " + corrected_string[-1])
                kelime = corrected_string
                puan_kazandir()
                baslangicKelimesi = corrected_string



    else:
        print("kelime eslesmiyor")
