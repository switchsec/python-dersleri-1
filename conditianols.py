#Conditianols =  şart
istenenKredi = 10000

hesap = 6001
düşükKredi = 0
minimumOlmasıGerekenHesap = 10000

if hesap>= minimumOlmasıGerekenHesap:
    print("Kredi verilebilir") 
elif hesap <= düşükKredi:
    print("Hesabınızda para bulunmamaktadır ")

elif hesap >=  9000 and hesap <= 9500: #Eğer hesap 9000 den büyük eşit ve 9500den küçük eşit ise bunu yazdır
    print("Araba ve motosiklet alabiliyorsunuz")

elif hesap >=  9501 and hesap <= 9900:
    print("Araba ve elektrikli motor alabiliyorsunuz") #Eğer hesap 9501 den büyük ve 9900 den küçük eşit ise bunu yazdır

elif hesap == 6000 or hesap >= 6000:
    print("Araba veya motor alabiliyorsun") #Eğer hesap 6000'e eşit veya hesap 6000den büyük ve eşit ise bunu yazdır 

else:
    print("Kredi almak için bakiyen yok orospu çocu")



print("İşlem sonu") # Burası if ile aynı yerde olduğu için if'in içine girmez 



#NOTLAR
# and kullanılıyorsa her ikiside olmak zorunda
# or kullanılıyorsa ikisinden biri olmak zorunda
# 
