""" Faktöriyel """


"""
sayi = int(input("Lütfen faktöriyel için bir sayı giriniz: "))

a = 1

for i in range(1,sayi+1):
       a = a*i

print("{}! = ".format(sayi)+str(a))

"""

mevcutmiktar = 2000

while True:
    işlem = int(input("Yapmak istediğiniz işlemi seçiniz: Para Çekme=>1,"
                      " Para Yatırma=>2, Kart Bilgileri=>3, Kart İade=>4:\n=>"))
    if işlem==1:
        print("Hesabınızdaki mevcut miktar: {}".format(mevcutmiktar))
        miktar= int(input("Lütfen çekmek istediğiniz miktarı giriniz:"))
        mevcutmiktar = mevcutmiktar-miktar
        print("Kalan Miktar: {}".format(mevcutmiktar))


    elif işlem==2:
        print("Hesabınızdaki mevcut miktar {}".format(mevcutmiktar))
        miktar = int(input("Lütfen yatırmak istediğiniz miktarı giriniz:"))
        mevcutmiktar = mevcutmiktar + miktar
        print("Hesabınızdaki mevcut miktar: {}".format(mevcutmiktar))

    elif  işlem==3:
        kartbilgileri={
            "isim" : "kullanıcı1",
            "soyisim" : "kullanıcısoyisim",
            "İban" : 123456,
            "paramiktarı" : mevcutmiktar
        }
        print(kartbilgileri.values())

    elif işlem==4:
        break