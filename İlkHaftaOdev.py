# ÖDEV1) Python'da Veri Tiplerini araþtýrýnýz, her bir veri tipi için kendi cümlelerinizle açýklamalar yazýnýz.

#String: Metinsel deðerleri ifade eder.Çift týrnak veya tek týrnak içerisinde yazýlan verilerdir.Örneðin: "Emre","Ali","35","F26","KayitliCalisan",'Murat','X'

#Int:negatif ve pozitif tam sayýlarý ifade eder. Örneðin 1,-10,999999,46,-45,0,150,26,-3,5,9
#Float: negatif ve pozitif ondalýklý sayýlarý temsil eder.Örneðin 3,14 86,94 -29,49 
#Complex: Bu veri türünde ise sayýlar daha çok ileri düzey matematik iþlemlerinde kullanýlmaktadýr.5b,-9a, 7+2b

#Sequence yani sýralama, dizi veri tipleri ise üçe ayrýlýr. 
#List birden fazla veri dizisini tek bir tipte birleþtirmeyi saðlar ve köþeli parantez içinde kullanýlýr.Örneðin MyList = ["Elma", "Üzüm", "Karpuz"]
#Range bir fonksiyon olarak çalýþmakla birlikte genellikle döngülerin içerisinde kullanýlýr.Örneðin range(-8,6,2) for döngüsüne içinde kullanýlýrsa -8'den 6ya kadar olan sayýlarý 2þer sýrayla altalta yazar
#Tuple ise parantez içinde çalýþan, dizi oluþturan bir yapýdýr ve sýralý bir biçimde oluþturulmaktadýr.Listten farký ise dizi içerisindeki verilerin deðiþtirilemez olmasý yani ekleme,güncelleme veya silme yapýlamaz.Örneðin MyTuple = (17, 34, 60)

#Dict(Dictionary) veri tipi:süslü parantez ile kullanýlýr.Bir anahtar kelime ve bir deðer barýndýrýr.Örneðin Arabam{"Marka":"Fiat","Model":"500X","Sene":2020}

#Set veri tipleri:Kümeler birden çok öðeyi tek bir deðiþken içerisinde tutmak için kullanýlýr ve süslü parantez ile yazýlýr. Set ve Frozenset olarak ikiye ayrýlýr.Örneðin  ThisSet= set{"apple", "banana", "cherry"}
 
#Bool veri tipi:Yalnýzca Doðru ve yanlýþ deðerlerini ifade eder.Örneðin: True,False

#Binary veri tipleri: 
#Bytes verilmiþ olan boyutta ve girilen verilerle baþlatýlan deðiþmez bir bayt nesnesini kendi içerisinde döndürür.Örneðin x=b"4"
#Bytearray byte veri tipinde oluþturulan veriler üzerinde deðiþiklik için yapmakta kullanýlýr. x=bytearray(4)
#Memoryview ise Python’da bellek durumunu görüntülemek için kullanýlýr.x=memoryview(bytes(4))



# SORU2) Kodlama.io sitesinde deðiþken olarak kullanýldýðýný düþündüðünüz verileri, veri tipleriyle birlikte örneklendiriniz.

# String veri tipi olarak kurslarým, tüm kurslar, kariyer, sýk sorulan sorular, kullaným koþullarý ve gizlilik politikasýný örnek gösterebiliriz.
# List veri tipine kategori ve eðitmenleri örnek verebiliriz. 
# Eðitim %25-%30 tamamlandýise integer veri tipine örnektir



# SORU3)Kodlama.io sitesinde þart bloklarý kullanýldýðýný düþündüðünüz kýsýmlarý örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

#KullaniciAdi="oemrec"
#Sifre="1597K."
#x = str(input("Kullanici adinizi giriniz:"))
#y = str(input("Sifrenizi giriniz:"))
#Giris=bool
#if (x==KullaniciAdi and y==Sifre):
#    Giris=True
#    print("Basariyla Giris Yaptiniz")
#else:
#    Giris=False
#    print("Kullanici Adi veya Sifre Hatali")