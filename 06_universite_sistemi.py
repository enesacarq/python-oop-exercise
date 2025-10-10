class UniversiteUyesi:
    def __init__(self,ad,unigiris,tel,kimlik):
        self.ad=ad
        self.unigiris=unigiris
        self.tel=tel
        self.kimlik=kimlik


class Ogrenci(UniversiteUyesi):
    def __init__(self,ad,unigiris,tel,kimlik):
        super().__init__(ad,unigiris,tel,kimlik)
        self.alinan_dersler=[]




    def ders_al(self,ders):
        self.alinan_dersler.append(ders)

    def alinan_dersleri_goster(self):
        for dersler in self.alinan_dersler:
            print(f"Ders:{dersler.ad} saat:{dersler.saat} dersi veren:{dersler.ogretimuyesi} kontejan:{dersler.kontejan}")


class Ders:
    def __init__(self,ad,saat,ogretimuyesi,kontejan):
        self.ad=ad
        self.saat=saat
        self.ogretimuyesi=ogretimuyesi
        self.kontejan=kontejan


class OgretimUyesi(UniversiteUyesi):
    def __init__(self,ad,unigiris,tel,kimlik,unvan,makalesayisi):
        super().__init__(ad,unigiris,tel,kimlik)
        self.unvan=unvan
        self.makalesayisi=makalesayisi
    
    def __str__(self):
        return f"{self.unvan} {self.ad} "



ogretimuyesi1=OgretimUyesi("Ahmet Daren",2018,5455444545,212342114241,"Docent Doktor",40)
ogrenci1=Ogrenci("Hasan Kacar",2023,546660777,569499449994)

mat1=Ders("Matematik1",4,ogretimuyesi1,50)

ogrenci1.ders_al(mat1)
ogrenci1.alinan_dersleri_goster()




