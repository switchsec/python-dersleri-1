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