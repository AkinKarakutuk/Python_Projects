print("*****Öğrenci Not Sistemi")

ogrencibilgi = input("Lütfen öğrenci ad ve soyadı giriniz:")

vize = int(input("Lütfen vize Notunuzu Giriniz: "))

final = int(input(("Lütfen Final Notunuzu Giriniz: ")))

ögrenciNot = (vize*0.4+final*0.6)

if(ögrenciNot >= 85 and ögrenciNot<=100 ):
    print("Başarı Notu:AA Notunuz: %d" %(ögrenciNot))

elif(ögrenciNot >=70 and ögrenciNot<85):
    print("Başarı Notu:BA Notunuz: %d" %(ögrenciNot))

elif(ögrenciNot >=60 and ögrenciNot<70):
    print("Başarı Notu:BB Notunuz: %d" %(ögrenciNot))

elif(ögrenciNot >=50 and ögrenciNot<60):
    print("Başarı Notu:CB Notunuz: %d" %(ögrenciNot))

elif(ögrenciNot >=40 and ögrenciNot<50):
    print("Başarı Notu:CC Notunuz: %d" %(ögrenciNot))

elif(ögrenciNot>=0 and ögrenciNot<=40):
    print("Başarı Notu:FF Notunuz: %d" % (ögrenciNot))

else:
    print("Lütfen not değerlerini 0 ile 100 arasında girin.")