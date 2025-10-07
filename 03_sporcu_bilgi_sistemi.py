class Sporcu:
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas
        self.antremanprogrami=None
        self.saglikbilgileri=None

    def saglik_bilgileri_ata(self,saglik_bilgileri):
        self.saglikbilgileri=saglik_bilgileri

    def antreman_programi_ata(self,antreman_programi):
        self.antremanprogrami=antreman_programi

    def performansi_goster(self):
        return f"{self.isim}-{self.yas}-{self.antremanprogrami}-{self.saglikbilgileri}"
    
class AntremanProgrami:
    def __init__(self,aktiviteler):
        self.aktiviteler=aktiviteler
    
    def __str__(self):
        return f"{', '.join(self.aktiviteler)}"


class SaglikBilgileri:
    def __init__(self,kilo,boy,nabiz,kanbasinci):
        self.kilo=kilo
        self.boy=boy
        self.nabiz=nabiz
        self.kanbasinci=kanbasinci

    def __str__(self):
        return f"Kilo:{self.kilo},Boy:{self.boy},Nabiz:{self.nabiz},Kan basinci:{self.kanbasinci}"
    

sporcu1=Sporcu("Enes Ferit",25)

saglik_sporcu1=SaglikBilgileri(70,1.80,84,90)
antremansporcu1=AntremanProgrami(["Kosu","Mekik","Sinav"])


sporcu1.antreman_programi_ata(antremansporcu1)
sporcu1.saglik_bilgileri_ata(saglik_sporcu1)
print(sporcu1.performansi_goster())
