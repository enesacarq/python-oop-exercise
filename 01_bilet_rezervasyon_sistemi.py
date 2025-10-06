class Etkinlik:
    def __init__(self,isim,tarih,yer):
        self.isim=isim
        self.tarih=tarih
        self.yer=yer
        self.biletler=[]

    
    def bilet_ekle(self,bilet):
        self.biletler.append(bilet)

    
    def biletleri_goster(self):
        for bilet in self.biletler:
            print(bilet)

class Bilet:
    def __init__(self,kategori,fiyat,isim):
        self.kategori=kategori
        self.fiyat=fiyat
        self.reserve_eden=isim

    def __str__(self):
        return f"{self.kategori}-{self.fiyat}, Reserve eden: {self.reserve_eden}"


konser=Etkinlik("Konser","12.12.12","Mardin")
bilet1=Bilet("VIP",200,"Enes Kilic")
bilet2=Bilet("Normal",250,"Ahmet Canli")

konser.bilet_ekle(bilet1)
konser.bilet_ekle(bilet2)

konser.biletleri_goster()


    

    