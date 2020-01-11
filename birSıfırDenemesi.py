from turkishnlp import detector

obj = detector.TurkishNLP()
obj.create_word_set()

if(obj.is_turkish("Ben bugün ankaraya gideceğim belki birşeyler alırım")):
    print("oley")

# detector.py içindeki  print(accuracy) satırını sil