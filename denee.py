from turkishnlp import detector

obj = detector.TurkishNLP()

# wordseti yükleme kodu çalıştırılacak

obj.create_word_set()

print("Bu oyun verilen kelimenin son harfi ile başlayan bir kelime yazan kullanıcıya puan kazandırmayı hedefler.")
print("Başlangıç kelimesi: BAŞARI ")


# EKLENECEKLER
# kelime ve uzunluğu kadar puan çarpanı


kelime = input()


#if : bir önceki kelimenin son harfi ile yeni girilen kelimenin ilk harfi aynıysa

if obj.is_turkish(kelime) == 1:
    print(kelime+" turkce")

    #kelime uzunluğu kadar puan çarpanı

else:
    print(kelime + " turkce degil bunu mu demek istediniz : ")
    lwords = obj.list_words(kelime)
    print(obj.auto_correct(lwords))

    #if turkish'e geri dön

#else if : yanlış kelime girdiniz tekrar deneyiniz