# -*- coding:utf-8 -*-
import hashlib
import json
import time
from Islem import Islem_Kodlayici 


class Blok:
    

    def __init__(self, timestamp, islemler, bir_onceki_hash_degeri=''):
        self.bir_onceki_hash_degeri = bir_onceki_hash_degeri
        self.timestamp = timestamp
        self.islemler = islemler
        self.nonce = 0
        self.hash = self.hash_hesapla()
        
#  blok başlatma
#  :parametre zaman damgası: oluşturulduğunda zaman damgası
#  :parametre işlemler: blok verileri
#  :parametre bir_onceki_hash_degeri: önceki bloğun özeti
#  :parametre hash: bloğun hash'i
#83C748B2EFCEE52EE855D03950FE983AD0C222A95E03C7E60F01A48428246310  selcukarden

#4E7E42B86050938DB4ACD1B1B0347D7F9BD1AAFBAAAB05A45BAA8C91CEDCA658  Selcukarden



    def hash_hesapla(self):
        islenMemis_ifade = self.bir_onceki_hash_degeri + str(self.timestamp) + json.dumps(self.islemler, ensure_ascii=False, cls=Islem_Kodlayici) + str(self.nonce)
        sha256 = hashlib.sha256()
        sha256.update(islenMemis_ifade.encode('utf-8'))
        hash = sha256.hexdigest()
        return hash
        
#  Blok hash değerini hesaplayın
#  :return:
# Blok bilgisini birleştirin ve sha256'nın hash değerini oluşturun
    
    def blogu_kaz(self, zorluk):

        zamanin_baslangici = time.process_time()
        # Hash değerinin ilk zorluk basamağının 0 olmasını zorunlu kılın
        while self.hash[0: zorluk] != ''.join(['0'] * zorluk):
            # gereksinimleri karşılama
            self.nonce += 1
            self.hash = self.hash_hesapla()
        print("Blogun Kazımı için:%s,  %fSaniye Sürdü" % (self.hash, time.process_time() - zamanin_baslangici))


#  Kazım
#  :parametre zorluk: zorluk
#  :return: