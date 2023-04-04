ogrenciler=[]
print (ogrenciler)
print("***************************************")

def OgrenciEkle(isim,soyisim):
    
    ogrenciler.append(isim+" "+soyisim)    
OgrenciEkle("Mete","Cingoz")
OgrenciEkle("Ali","Doruk")
OgrenciEkle("Sahabbettin","Kilic")
OgrenciEkle("Barbaros","Hayreddin")
OgrenciEkle("Selim","Mercan")
print(ogrenciler) 
print("*************************************")

def OgrenciSil(isim,soyisim):
    ogrenciler.remove(isim+" "+soyisim) 
OgrenciSil("Sahabbettin","Kilic")
print(ogrenciler)
print("*************************************")

def birdenCokOgrenciEkle(ogrenci):
    ogrenciler.extend(ogrenci)
birdenCokOgrenciEkle(["Zeynep Ahmet", "Ruya Cakmak","Onur Emre","Ender Emre","Murad Birinci","Rustem Kor","Emre Cakmak"])
print(ogrenciler)
print("*************************************")

def goster(ogrenciler):
    i=0
    while i<len(ogrenciler):
        print(ogrenciler[i])
        i+=1
goster(ogrenciler)
print("*************************************")

def ogrenciNoOgren(isim,soyisim):
    OgrNo=ogrenciler.index(f"{isim} {soyisim}")
    print(OgrNo)
ogrenciNoOgren("Murad","Birinci")
ogrenciNoOgren("Onur","Emre")
print("*************************************")

def CokOgrSil(*silinecekler):
    for o in silinecekler:
        ogrenciler.remove(o)
CokOgrSil("Onur Emre","Ruya Cakmak")
goster(ogrenciler)
