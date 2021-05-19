urunler = ["Laptop", "Mause", "Keyboard"]
print(urunler)
#print(type(urunler))#Çıktısı <class 'list'>
urunler.append("Telefon") #urunlere telefon ekler 
print(urunler)
                #0        #1       #2
ogrenciler1 = ["İlker", "Cavit", "Berkay"] #Buraya 101 diyelim
ogrenciler2 = ["Kerem", "Halil", "Murat"] #Buraya 102 diyelim
#Burası list şeklinde olduğu için biz öğrenciler1'e sen 101'i tut öğrenciler2'ye ise sen 102'yi tut diyoruz
ogrenciler1 = ogrenciler2 #Öğrenciler1 ' e diyoruzki sen 101'i bırak artık 102'yi tutuyorsun yani bu sayedede 101 gidiyor tutan olmadığı için
ogrenciler2[0]= "Ahmet" #Ogrenciler 2'nin 0.elemanını değiştiriyoruz yani ilker'i
print(ogrenciler1) #Ardından burası ogrenciler2'yi yazdırıyor yani çıktısı ahmet,halil,murat olarak yazdırıyor bunun nedeni ise ogrenciler1 = ogrenciler2 kod bloğunun olması


sayi1 = 10
sayi2 = 20
sayi1 = sayi2 #Sayi1 'i sayi2 ye eşitliyoruz yani sayi1 artık sayi 2 oluyor yaani sayi1= 20 , sayi2 = 20 sayi2'ye dokunulmaz
sayi2= 60 
print(sayi2) # Çıktısı 60
print(sayi1) # Çıktısı 20 


isim1= "Ahmet"
print(isim1[0]) #Str'ler bir list'dir bu yüzdende referans tipine girer ama çıktılarda değertipi olarak gözükür



#NOT 
#REFERANS TİP -> List
#DEĞER TİP -> İNT 
#  