#döngüler

sehirler = ["Ankara", "İstanbul", "İzmir"]

for sehir in sehirler: #şehirlerin içinde dolaş
    print(sehir) #Tüm şehirleri alt alta yazdır

for sayi in range(1,10,2): 
    print(sayi)#1 den başlayıp ikişer ikişer yaz 


sayac = 1  
while sayac <= 10:
    print(sayac) 
    sayac = sayac + 1



isim = input("Adınız :")
print("İsim : " + isim)


sayi = int(input("Kaçın faktöriyelini hesaplayayım : "))

faktöriyel = 1
if sayi<0:
    print("Negatif sayıları hesaplayamam")
elif sayi==0:
    print("Sonuç : 1")
else :
    for i in range(1,sayi+1):
        faktöriyel = faktöriyel * i 
    print("Sonuç : ", faktöriyel)


#NOT 
#5 faktöriyel -> 5*4*3*2*1