isim = "Ahmet"
yaş = 15

print(f'Ben {isim} {yaş} yaşındayım')

isimler = ["Ali","Ahmet","Mehmet","Cem","Görkem"]
isimler.append("Ayşe")
isimler.remove("Ahmet")
isimler.sort()
print("Toplamda şu kadar kullanıcı var : " +str( len(isimler)))
print(isimler)

kullanıcı1 = {
    "first_name" :"Ahmet",
    "last_name" : "Kubaş",
    "age" : "15",
    "data_create" : "2.04.2021"
}

print(kullanıcı1)




#NOTLAR 
#LİSTEDE İKİ İSİM YAZDIRILMAZ
#isimler.clear() siler
#del(kullanıcı1["age"]) 
#print(kullanıcı1["first_name"])
#print(kullanıcı1.get("last_name"))
