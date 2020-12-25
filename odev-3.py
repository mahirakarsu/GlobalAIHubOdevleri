import random

# tahmin.lower() dönüşümünde hata almamak için Türkçe karater kullanılmadı
kelimeDizi = ["mavi","nijerya","balik","çiğlik","okyanus","kağit","laptop"]

# rassal index. kelime listesinin uzunlugu ile sınırlı
kelimeIndex = random.randint(0,len(kelimeDizi)-1)

# kelime listeden secildi
sorulacakKelime = kelimeDizi[kelimeIndex]

isim = input("isim giriniz :")
print("hos geldin " + isim)

yanlisSayaci =0
dogruSayaci =0

harf =""
kelimeTahmin=""


while(yanlisSayaci < 6 ):
    tahmin = input("bir harf tahmini yapın ya da kelimeyi tahmin edin")
    # kelime - harf kontrolu
    # kelime tahmin edildiyse, kelimenin dogrulugunun kontrolu
    
    if len(tahmin) > 1:
        
        kelimeTahmin = tahmin.lower()
        if kelimeTahmin == sorulacakKelime:
            print("bildiniz. Kelime : " + sorulacakKelime)
            break
        else:
            print("yanlış tahmin")
            # kelime yanlış tahmin edilirse, harf sorulmaya devam edilir
            # kelime tahmini sayacları etkilemez. oyun devam eder
            continue
    else:
        # kelime tahmin edilmemiş, harf girişi yapılmış. 
        harf = tahmin.lower()
        

    
  
        
     # girdi harf ise, harfin kontrolu ve sayaclarin arttirilmasi
    if harf in sorulacakKelime:
        print("dogru tahmin")
        dogruSayaci+=1
    else:
        print("yanlış tahmin")
        yanlisSayaci+=1
        
        
        # tum harfler tahmin edilerek mi bulundu?
        
    if dogruSayaci == len(sorulacakKelime):
        
        print("kelime : " + sorulacakKelime)
        break

print("oyun sona erdi")