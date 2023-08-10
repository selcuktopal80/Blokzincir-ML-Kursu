# -*- coding:utf-8 -*-
from Blok import Blok
import time
from Islem import Islem


class Blokzincir:
    def __init__(self):
        # Zinciri başlat, genesis bloğunu ekle
        self.zincir = [self.baslangic_blogu_olustur()]
        # İlk zorluğu ayarla
        self.zorluk = 6
        # bekleyen işlemler
        self.bekleyen_islemler = []
        # Madencilik ödülü belirleyin
        self.kazim_odulu = 50

    @staticmethod
    def baslangic_blogu_olustur():
        '''
        Genesis Bloğu Oluştur
         :return: Başlangıç ​​bloğu
         '''
        timestamp = time.mktime(time.strptime('2018-06-11 00:00:00', '%Y-%m-%d %H:%M:%S'))
        blok = Blok(timestamp, [], '')
        return blok

    def son_blogu_al(self):
        return self.zincir[-1]

# Zincirdeki son bloğu alın
# :return: son blok
 

    def blok_ekle(self, blok):

        blok.bir_onceki_hash_degeri = self.son_blogu_al().hash
# kazıma başla
        blok.blogu_kaz(self.zorluk)
# kazımdan sonra zincire ekle
        self.zincir.append(blok)
       
# blok ekle
# :parametre blok: eklemek için engelle
# :return:
        
    def islem_ekle(self, islem):
        self.bekleyen_islemler.append(islem)

#  işlem ekle
#  :param işlemi: yeni işlem
#  :return:
#  İşlemin bir dizi doğrulaması olmalıdır
# Bekleyen işlemlere ekle
        

    def bekleyen_islemi_kaz(self, kazanin_odul_hesabi):
        blok = Blok(time.time(), self.bekleyen_islemler, self.zincir[-1].hash)
        blok.blogu_kaz(self.zorluk)
        self.zincir.append(blok)
        self.bekleyen_islemler = [Islem(None, kazanin_odul_hesabi, self.kazim_odulu)]
        

#  Kazım bekleyen işlemler
#  :param kazanin_odul_hesabi: kazım ödül hesabı
#  :return:
# Başarılı kazımın ardından, bekleyen işlemleri sıfırlayın ve bir işlem ekleyin, bu kazımın ödülüdür
        

    def hesap_bakiyesini_al(self, hesap):
        '''
         para bakisyesini almak
         :param adresi: hesap
         :return: bakiye
         '''
        bakiye = 0
        for blok in self.zincir:
            for isls in blok.islemler:
                if isls.hesapTan == hesap:
                    # self başlatılan işlem harcaması
                    bakiye -= isls.miktar
                if isls.hesaBa == hesap:
                    # Kazanç
                    bakiye += isls.miktar
        return bakiye

    def blokzinciri_dogrula(self):
        '''
        Blockchain verilerinin eksiksiz olduğunu ve tahrif edilmediğini doğrulayın
         :return: sonucu kontrol et
         '''
        for i in range(1, len(self.zincir)):
            suAnki_blok = self.zincir[i]  # Şu anda üzerinde gidilen blok
            onceki_blok = self.zincir[i - 1]  # Geçerli bloğun önceki bloğu
            if suAnki_blok.hash != suAnki_blok.hash_hesapla():
                # Geçerli bloğun hash değeri, hesaplanan hash değerine eşit değilse, veri değişmiş demektir.
                return False
            if suAnki_blok.bir_onceki_hash_degeri != onceki_blok.hash_hesapla():
                # Mevcut bloğa kaydedilen önceki bloğa ait hash değeri, önceki bloğa ait hesaplanan hash değerine eşit değilse, önceki bloğa ait verilerin değiştiği veya
                # bu bloğa kaydedilen önceki bloğa ait hash değerinin değiştiği anlamına gelir
                return False
        return True


if __name__ == '__main__':
    blokzincir = Blokzincir() 
    print('address1  ', blokzincir.hesap_bakiyesini_al('address1'))
    print('address2  ', blokzincir.hesap_bakiyesini_al('address2'))
    print('address3  ', blokzincir.hesap_bakiyesini_al('address3'))
    print("---------------------------------")
    blokzincir.islem_ekle(Islem('address1', 'address2', 80))
    blokzincir.islem_ekle(Islem('address2', 'address3', 13))
    # address3 
    blokzincir.bekleyen_islemi_kaz('address3')
    print("---------------------------------")
    print('address1  ', blokzincir.hesap_bakiyesini_al('address1'))
    print('address2  ', blokzincir.hesap_bakiyesini_al('address2'))
    print('address3 ', blokzincir.hesap_bakiyesini_al('address3'))
    # address2 
    blokzincir.bekleyen_islemi_kaz('address2')
    print('address1  ', blokzincir.hesap_bakiyesini_al('address1'))
    print('address2  ', blokzincir.hesap_bakiyesini_al('address2'))
    print('address3  ', blokzincir.hesap_bakiyesini_al('address3'))
    print(blokzincir.son_blogu_al)
    print(blokzincir.kazim_odulu)
    blokzincir.baslangic_blogu_olustur

