class Konaklama: ##otel
    def __init__(self,isim,konum,odasayisi):
        self.isim=isim
        self.konum=konum
        self.odasayisi=odasayisi
        self.rezervasyonlar=[]


    def rezervasyon_yap(self,odasayisi,musteri):
        if odasayisi <=self.odasayisi :
            self.odasayisi-=odasayisi
            self.rezervasyonlar.append((musteri,odasayisi))
            musteri.rezervasyonlar.append({"isim":self.isim,"konum":self.konum,"oda":self.odasayisi})
            print("Rezervasyon basarili")
        else:
            print("Su anda oda yok malesef")
    
    def tum_rezervasyonlari_gor(self):
        for musteri,oda in self.rezervasyonlar:
            print(musteri,oda)

class Musteri:
    def __init__(self,isim):
        self.isim=isim
        self.rezervasyonlar=[]

    def __str__(self):
        return f"Musteri isim-soyisim:{self.isim}"
    
    def tum_rezervasyonlari_gor(self):
        for rezervasyon in self.rezervasyonlar:
            print(rezervasyon)


class Ucus:
    def __init__(self,ucus_no,kalkis,varis):
        self.ucus_no=ucus_no
        self.kalkis=kalkis
        self.varis=varis

    def ucus_bilgileri(self):
        print(f"Ucus no:{self.ucus_no},kalkis:{self.kalkis},varis:{self.varis}")


class AracKiralama:
    def __init__(self,isim,konum,arac_sayisi):
        self.isim=isim
        self.konum=konum
        self.arac_sayisi=arac_sayisi
        self.rezervasyonlar=[]

    def arac_kirala(self,arac_sayisi,musteri):
        if self.arac_sayisi>arac_sayisi:
            self.arac_sayisi-=arac_sayisi
            self.rezervasyonlar.append((musteri,arac_sayisi))
            musteri.rezervasyonlar.append({"isim":self.isim,
                                           "konum":self.konum,
                                           "arac_sayisi":arac_sayisi})
            print("Arac kiralama basarili")
        else:
            print("su an icin araba kalmadi")
    
    def tum_rezervasyonlari_gor(self):
        for musteri,arac_sayisi in self.rezervasyonlar:
            print(musteri,arac_sayisi)



musteri1=Musteri("Enes Kadir")
otel1=Konaklama("Comfort Hotel","Istanbul",50)
aracfirmasi1=AracKiralama("rent a car","Diyarbakir",25)

otel1.rezervasyon_yap(2,musteri1)
aracfirmasi1.arac_kirala(2,musteri1)

aracfirmasi1.tum_rezervasyonlari_gor()
otel1.tum_rezervasyonlari_gor()
musteri1.tum_rezervasyonlari_gor()


