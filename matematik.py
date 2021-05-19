
class Matematik:
    def __init__(self,sayi1,sayi2):#burdaki sayi1,sayi2 ile alttaki sayi1 , sayi2 aynı şeyler değildir
        self.sayi1 = sayi1 
        self.sayi2 = sayi2
        print("Matematik Başladı") 
    def topla(self):
        return self.sayi1 + self.sayi2 #matematiğin içindeki sayi2
    def cikar(self):
        return self.sayi1 - self.sayi2
    def böl(self):
        return self.sayi1 / self.sayi2
    def carp(self):
        return self.sayi1 * self.sayi2

matematik = Matematik(int(input("İlk sayıyı Giriniz")),int(input("İkince sayıyı giriniz")))
sonuc = matematik.böl()
print("Sonuç : " + str(sonuc))




#Developer switchsec
#İnstagram :  @_ahmetonlinee / @ahmetwitch
#Github : switchsec
