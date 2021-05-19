totalKullanıcılar = ["Ahmet", "Ali", "Mehmet", "Görkem","Tevfik", "Ayşe", "Fatma"]
sıfırKullanıcı = [""]

normalKullanıcılar = ["Ahmet" , "Ali" , "Mehmet"]
vipkull = ["Görkem", "Tevfik"]
adminKull = ["Ayşe", "Fatma"]
kullanıcı1 = vipkull
kullanıcı2 = adminKull
kullanıcı3 = normalKullanıcılar

for kullanıcı in totalKullanıcılar:
    if kullanıcı == normalKullanıcılar[0] :
        print("Normal Kullanıcılar"+ str(kullanıcı3))
    elif kullanıcı == vipkull[0] :
        print("Vip kullanıcılar"+ str(kullanıcı1))
    elif kullanıcı == adminKull[0] :
        print("Adminlerimiz" + str(kullanıcı2))
    elif kullanıcı == sıfırKullanıcı : 
        print("Kullanıcı Bulunamadı")
 

 #NOTLAR 
 #BUNU VERİ TABANI İLE BİRLEŞTİR