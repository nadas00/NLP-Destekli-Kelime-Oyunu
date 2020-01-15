
# Kelime oyununun basit konsol versiyonudur. Fonksiyonlar değişiklik gösterebilir.

# 1 kere çalıştırdıktan sonra obj.download() satırını siliniz

from turkishnlp import detector

obj = detector.TurkishNLP()
obj.download()
obj.create_word_set()

my_array = []
i = 0
toplampuan = 0

baslangicKelimesi = "başarı"

print("\nBu oyun verilen kelimenin son harfi ile başlayan bir kelime yazan kullanıcıya puan kazandırmayı hedefler. \n"
      "Başlagıç kelimesi -başarı-\n"
      "kelime giriniz...")

def puan_kazandir():

    bonus = 0

    global toplampuan
    kelimeUzunlugu = len(kelime)
    puan = kelimeUzunlugu * 4

    if(obj.is_vowel_harmonic(kelime)):
     print("%10 büyük ünlü uyumu bonusu ! ")
     bonus = bonus + 0.1

    if obj.is_turkish_origin(kelime):
     print("%20 Türkçe köken uyumlu sözcük bonusu ! ")
     bonus = bonus + 0.2

    toplambonus = bonus + 1
    puan = puan * toplambonus
    toplampuan = toplampuan + puan

    print(kelime + " kelimesinden " + str(puan) + " kazandınız!\n")


while i<6:
    kelime = input()

    if kelime.startswith(baslangicKelimesi[-1]):

        if obj.is_turkish(kelime):
            puan_kazandir()
            baslangicKelimesi = kelime
            my_array.append(kelime)
            i=i+1

        else:
            lwords = obj.list_words(kelime)
            corrected_words = obj.auto_correct(lwords)
            corrected_string = " ".join(corrected_words)
            if obj.is_turkish(corrected_string) and corrected_string[0] == baslangicKelimesi[-1]:
                print(
                    '"' + kelime + '"' + " Türkçe bir kelime değil " + '"' + corrected_string + '"' + " demek istemiş olabilirsiniz")
                print("-->Son Harf : " + corrected_string[-1])
                kelime = corrected_string
                puan_kazandir()
                baslangicKelimesi = corrected_string
                my_array.append(kelime)
                i = i + 1
            else:
                print("Bu kelime Türkçe değil birdaha deneyin!")

    else:
        print("Kelime eşleşmiyor")


print("\n toplampuan " + str(toplampuan))
print(my_array)
