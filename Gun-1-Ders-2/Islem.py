# -*- coding:utf-8 -*-
import json


class Islem:
    def __init__(self, hesapTan, hesaBa, miktar):
        self.hesapTan = hesapTan
        self.hesaBa = hesaBa
        self.miktar = miktar
        
#  İşlemi başlat
#  :param hesapTan: işlem başlatıcı
#  :param hesaBa: işlem alıcısı
#  :param tutarı: işlem miktarı

class Islem_Kodlayici(json.JSONEncoder):
    def default(self, onun):
        if isinstance(onun, Islem):
            return onun.__dict__
        return json.JSONEncoder.default(self, onun)


if __name__ == '__main__':
    # Deneme
    isl = Islem('Selcuk', 'Arden', 100)
    print(isl)
    print(json.dumps(isl, ensure_ascii=False, cls= Islem_Kodlayici))


