class Musteri:
    def __init__(self,isim,email,tel):
        self.isim=isim
        self.email=email
        self.tel=tel
        self.kisi_satislar=[]

    def satis_ekle(self,tarih,urun):
        yeni_satis=Satis(tarih,urun)
        self.kisi_satislar.append(yeni_satis)

    
class Satis:
    tum_satislar=[]

    def __init__(self,tarih,urun):
        self.tarih=tarih
        self.urun=urun
        Satis.tum_satislar.append(self) 

    def __str__(self):
        return f"Satis tarihi:{self.tarih}, Satis tutari:{self.urun.fiyat}, Urun:{self.urun}"
    
class Urun:
    def __init__(self,isim,fiyat,renk=None):
        self.isim=isim
        self.fiyat=fiyat
        self.renk=renk

    def __str__(self):
        return f"Urun ismi:{self.isim}, Urun fiyati: {self.fiyat}, urun renk bilgisi:{self.renk}"
    

class SatisYonetimi:
    @staticmethod
    def tum_satislari_goruntule():
        for satis in Satis.tum_satislar:
            print(satis)


    @staticmethod
    def belirli_tarihteki_satislari_goruntule(tarih):
        pass


    @staticmethod
    def fiyat_araligindeki_satislari_goruntule(minimum,maksimum):
        pass


ali=Musteri("Ali","ali3459@gmail.com",54534343434)

telefon1=Urun("Iphone 13","45000","gri")
telefon2=Urun("Iphone 13 Pro",50000,"Lacivert")

ali.satis_ekle("10.10.2025",telefon1)
ali.satis_ekle("12.12.2025",telefon2)

SatisYonetimi.tum_satislari_goruntule()
