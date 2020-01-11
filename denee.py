from turkishnlp import detector

obj = detector.TurkishNLP()

# wordseti yükleme kodu çalıştırılacak

obj.create_word_set()

print("Bu oyun verilen kelimenin son harfi ile başlayan bir kelime yazan kullanıcıya puan kazandırmayı hedefler.")
print("Başlangıç kelimesi: BAŞARI ")

# EKLENECEKLER
# kelime ve uzunluğu kadar puan çarpanı


baslangicKelimesi = "başarı"
kelime = input()

# bir önceki kelimenin son harfi ile yeni girilen kelimenin ilk harfi aynıysa


if kelime.startswith(baslangicKelimesi[-1]):


 if obj.is_turkish(kelime):
  print(kelime + " turkce")
  baslangicKelimesi = kelime

  # kelime uzunluğu kadar puan çarpanı

 else:
   lwords = obj.list_words(kelime)
   dogrusu = (obj.auto_correct(lwords))
   if obj.is_turkish(dogrusu):
    print(kelime + " turkce degil bunu mu demek istediniz : ")
    baslangicKelimesi = dogrusu
    # if turkish'e geri dön

else:
 print("kelime eslesmiyor")

# else if : yanlış kelime girdiniz tekrar deneyiniz
