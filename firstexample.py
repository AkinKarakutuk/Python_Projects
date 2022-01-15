import math

print("""Hipotenüs Değeri""")

sayi1 = int(input("lütfen birinci kenarı  giriniz: "))
sayi2 = int(input("Lütfen ikinci kenarı giriniz: "))

print("Hipotenüs değeri:" ,math.sqrt(sayi1**2+sayi2**2))




print("""Akım Hesaplanması""")

gerilim = float(input("lütfen gerilim değerini giriniz giriniz: "))

direnç = float(input("Lütfen direnç değerini giriniz: "))

while True:
    if direnç == 0:
        direnç = float(input("Direnç değeri sıfır olamaz : "))
    else:
        break

Akim = float(gerilim/direnç)

print("Akım Değeri:%f" %(Akim))



print("""Sözlük""")

kelimeler = dict()

ingkelime = input("İngilizce kelimeyi giriniz: ")
ceviri = input("Türkçe karşılıpını giriniz: ")

kelimeler[ingkelime] = ceviri

ingkelime = input("İngilizce kelimeyi giriniz: ")
ceviri = input("Türkçe karşılıpını giriniz: ")

kelimeler[ingkelime] = ceviri

ingkelime = input("İngilizce kelimeyi giriniz: ")
ceviri = input("Türkçe karşılıpını giriniz: ")

kelimeler[ingkelime] = ceviri

ingkelime = input("İngilizce kelimeyi giriniz: ")
ceviri = input("Türkçe karşılıpını giriniz: ")

kelimeler[ingkelime] = ceviri

ingkelime = input("İngilizce kelimeyi giriniz: ")
ceviri = input("Türkçe karşılıpını giriniz: ")

kelimeler[ingkelime] = ceviri

print(kelimeler)