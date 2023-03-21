# �DEV1) Python'da Veri Tiplerini ara�t�r�n�z, her bir veri tipi i�in kendi c�mlelerinizle a��klamalar yaz�n�z.

#String: Metinsel de�erleri ifade eder.�ift t�rnak veya tek t�rnak i�erisinde yaz�lan verilerdir.�rne�in: "Emre","Ali","35","F26","KayitliCalisan",'Murat','X'

#Int:negatif ve pozitif tam say�lar� ifade eder. �rne�in 1,-10,999999,46,-45,0,150,26,-3,5,9
#Float: negatif ve pozitif ondal�kl� say�lar� temsil eder.�rne�in 3,14 86,94 -29,49 
#Complex: Bu veri t�r�nde ise say�lar daha �ok ileri d�zey matematik i�lemlerinde kullan�lmaktad�r.5b,-9a, 7+2b

#Sequence yani s�ralama, dizi veri tipleri ise ��e ayr�l�r. 
#List birden fazla veri dizisini tek bir tipte birle�tirmeyi sa�lar ve k��eli parantez i�inde kullan�l�r.�rne�in MyList = ["Elma", "�z�m", "Karpuz"]
#Range bir fonksiyon olarak �al��makla birlikte genellikle d�ng�lerin i�erisinde kullan�l�r.�rne�in range(-8,6,2) for d�ng�s�ne i�inde kullan�l�rsa -8'den 6ya kadar olan say�lar� 2�er s�rayla altalta yazar
#Tuple ise parantez i�inde �al��an, dizi olu�turan bir yap�d�r ve s�ral� bir bi�imde olu�turulmaktad�r.Listten fark� ise dizi i�erisindeki verilerin de�i�tirilemez olmas� yani ekleme,g�ncelleme veya silme yap�lamaz.�rne�in MyTuple = (17, 34, 60)

#Dict(Dictionary) veri tipi:s�sl� parantez ile kullan�l�r.Bir anahtar kelime ve bir de�er bar�nd�r�r.�rne�in Arabam{"Marka":"Fiat","Model":"500X","Sene":2020}

#Set veri tipleri:K�meler birden �ok ��eyi tek bir de�i�ken i�erisinde tutmak i�in kullan�l�r ve s�sl� parantez ile yaz�l�r. Set ve Frozenset olarak ikiye ayr�l�r.�rne�in  ThisSet= set{"apple", "banana", "cherry"}
 
#Bool veri tipi:Yaln�zca Do�ru ve yanl�� de�erlerini ifade eder.�rne�in: True,False

#Binary veri tipleri: 
#Bytes verilmi� olan boyutta ve girilen verilerle ba�lat�lan de�i�mez bir bayt nesnesini kendi i�erisinde d�nd�r�r.�rne�in x=b"4"
#Bytearray byte veri tipinde olu�turulan veriler �zerinde de�i�iklik i�in yapmakta kullan�l�r. x=bytearray(4)
#Memoryview ise Python�da bellek durumunu g�r�nt�lemek i�in kullan�l�r.x=memoryview(bytes(4))



# SORU2) Kodlama.io sitesinde de�i�ken olarak kullan�ld���n� d���nd���n�z verileri, veri tipleriyle birlikte �rneklendiriniz.

# String veri tipi olarak kurslar�m, t�m kurslar, kariyer, s�k sorulan sorular, kullan�m ko�ullar� ve gizlilik politikas�n� �rnek g�sterebiliriz.
# List veri tipine kategori ve e�itmenleri �rnek verebiliriz. 
# E�itim %25-%30 tamamland�ise integer veri tipine �rnektir



# SORU3)Kodlama.io sitesinde �art bloklar� kullan�ld���n� d���nd���n�z k�s�mlar� �rneklendiriniz ve Python dilinde bu �rnekleri koda d�k�n�z.

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