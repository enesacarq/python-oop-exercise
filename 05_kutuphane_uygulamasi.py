import datetime

class Yayin:
    def __init__(self,baslik,yazar,yayinci):
        self.baslik=baslik
        self.yazar=yazar
        self.yayinci=yayinci
        self.odunc_alindi=False

    def odunc_ver(self):
        if not self.odunc_alindi:
            self.odunc_alindi=True
    
    def geri_al(self):
        if self.odunc_alindi:
            self.odunc_alindi=False


class Kullanici:
    def __init__(self,isim,kimlikno,tel,kullanici_turu="Ogrenci"):
        self.isim=isim
        self.kimlikno=kimlikno
        self.tel=tel
        self.kullanici_turu=kullanici_turu
        self.odunc_alinan_yayinlar=[]
        self.maks_odunc_yayin=30 if kullanici_turu=="Ogretim Gorevlisi" else 10
        self.maks_odunc_sure=30 if kullanici_turu=="Ogretim Gorevlisi" else 15
        

    def odunc_al(self,yayin):
        if len(self.odunc_alinan_yayinlar)< self.maks_odunc_yayin:
            if not yayin.odunc_alindi:
                yayin.odunc_ver()
                self.odunc_alinan_yayinlar.append((yayin,datetime.date.today()))
                print("Odunc alma islemi basarili")
            else:
                print("Odunc alma islemi sirasinda bir sorun olustu.")
        else:
            print("Maksimum odunc alabileceğiniz yayin sayisina ulastiniz.")

    
    def geri_iade(self,yayin):
        for odunc_alinan_yayin,odunc_alma_tarihi in self.odunc_alinan_yayinlar:
            if odunc_alinan_yayin==yayin:
                iade_tarihi=datetime.date.today()
                toplam_sure=(iade_tarihi-odunc_alma_tarihi).days

                if toplam_sure > self.maks_odunc_sure:
                    print("iade tarihi coktan gecti")

                yayin.geri_al()
                self.odunc_alinan_yayinlar.remove((odunc_alinan_yayin,odunc_alma_tarihi))
                print("geri iade basarili")

            else:
                print("geri iade sirasinda sorun olustu.")

yayin1=Yayin("Sozler","Said Nursi","Envar Neşriyat")
kullanici1=Kullanici("Enes Adel",52123141241,5455454546)

kullanici1.odunc_al(yayin1)
kullanici1.geri_iade(yayin1)

