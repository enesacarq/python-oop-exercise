class AkilliCihaz:
    def __init__(self,oda):
        self.oda=oda
        self.acik=False

    def ac(self):
        self.acik=True
    
    def kapat(self):
        self.acik=False

class Isik(AkilliCihaz):
    def __init__(self,oda,renk):
        super().__init__(oda)
        self.renk=renk
    
    def renk_degistir(self,renk):
        self.renk=renk
    
class Klima(AkilliCihaz):
    def __init__(self,oda,sicaklik):
        super().__init__(oda)
        self.sicaklik=sicaklik
    
    def sicaklik_degistir(self,sicaklik):
        self.sicaklik=sicaklik

class KahveMakinesi(AkilliCihaz):
    pass

class GuvenlikKamerasi(AkilliCihaz):
    def kayit_baslat(self):
        if not self.acik:
            self.acik=True
    
    def kayit_sonlandir(self):
        if self.acik:
            self.acik=False


isik1=Isik("oturma odasi","beyaz")
isik1.ac()

klima=Klima("salon",20)
klima.kapat()

kahvemakinesi=KahveMakinesi("mutfak")
kahvemakinesi.kapat()

kamera1=GuvenlikKamerasi("Salon")
kamera2=GuvenlikKamerasi("Disari")
kamera3=GuvenlikKamerasi("Arka balkon")

kamera1.kayit_baslat()
kamera2.kayit_baslat()
kamera3.kayit_baslat()


print(isik1.acik,klima.acik,kahvemakinesi.acik,kamera3.acik)
