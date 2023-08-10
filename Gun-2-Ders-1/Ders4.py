
#Sepolia network e SÖzleşme Deployment ve Etkileşim

from solcx import compile_standard
import json
from web3 import Web3

#sozlesme compile edip json dosyasini oluştururalım


with open("./MerhabaDunya.sol","r") as file:
    MerhabaDunya_dosyasi = file.read()
    # print(MerhabaDunya_dosyasi)


compile_edilmis_sol = compile_standard(
    
    {"language": "Solidity", 

     "sources" : {"MerhabaDunya.sol": {"content":  MerhabaDunya_dosyasi}}, 

     "settings": {
        
        "outputSelection":{
            
            "*":{"*":["abi","metadata","evm.bytecode","evm.sourceMap"]}
           
            } 
            
        },
      
    }, 
    solc_version= "0.8.0", 
    )



with open("compile_edilmis_sol.json", "w") as file:
    json.dump(compile_edilmis_sol, file)


#abi kodu alalım
MerhabaDunya_abi= compile_edilmis_sol["contracts"]["MerhabaDunya.sol"]["MerhabaDunya"]["abi"]

#bytecodu alalım
MerhabaDunya_bytecode = compile_edilmis_sol["contracts"]["MerhabaDunya.sol"]["MerhabaDunya"]["evm"]["bytecode"]["object"]


saglayici_url = "https://eth-sepolia.g.alchemy.com/v2/nVi73JnHYC2aCDzhC3hzpGl8GEPiUDQk"

web3_baglantisi= Web3(Web3.HTTPProvider(saglayici_url))

print(bool(web3_baglantisi))


zincir_id= 11155111 #https://chainlist.org/chain/11155111

adresim = "" #metamask

adres_gizli_anahtari= ""

# #Sozlesmeyi Python içinde oluşturacağız, bir instance sini alacağız

MerhabaDunyaJson_Ornegi = web3_baglantisi.eth.contract(abi=MerhabaDunya_abi, bytecode = MerhabaDunya_bytecode )

print(MerhabaDunyaJson_Ornegi)

nonce_degeri = web3_baglantisi.eth.get_transaction_count(adresim)

# # 1) İşlem oluşturma
# # 2) İşlem imzalama
# # 3) İşlemi gönderme

islem = MerhabaDunyaJson_Ornegi.constructor().build_transaction({"from": adresim, "nonce": nonce_degeri })

print(islem)


imzalanmis_islem = web3_baglantisi.eth.account.sign_transaction(islem, private_key=adres_gizli_anahtari) #signed tx

islem_hashi = web3_baglantisi.eth.send_raw_transaction(imzalanmis_islem.rawTransaction) #tx hash

# '''Temel olarak bir ham işlem, bir işlemin imzası eklenmiş bir makine temsilidir.'''

islem_adisyon = web3_baglantisi.eth.wait_for_transaction_receipt(islem_hashi) #reciept

print(islem_adisyon)

Merhaba_Dunya_TestNetteyiz = web3_baglantisi.eth.contract(address= islem_adisyon.contractAddress,  abi= MerhabaDunya_abi)

print(Merhaba_Dunya_TestNetteyiz)


print(Merhaba_Dunya_TestNetteyiz.functions.SonucYazdir().call())

print("tamamdir", Merhaba_Dunya_TestNetteyiz.functions.mesajiAyarla("selamKurs").call())

print("devamdir", Merhaba_Dunya_TestNetteyiz.functions.mesajiSoyle().call())

#call yaptğimiz için blockchain içinde herhangi bir state değişimine sebep olmuyor.
#blokchaine e kayıt ve state veya değişken değişimi için mutlaka transaction yapmalıyız
#yine 3 adimda yapıyoruz

#1 işlem oluştur
mesaji_ayarla_islemi = Merhaba_Dunya_TestNetteyiz.functions.mesajiAyarla("selamKurs").build_transaction({"from": adresim, "nonce": nonce_degeri +1 })

#2 işlemi imzala
imzalanmis_mesaji_ayarla_islemi = web3_baglantisi.eth.account.sign_transaction(mesaji_ayarla_islemi, private_key=adres_gizli_anahtari)

#3 imzalanmış işlemi gönder

mesaj_ayarla_islem_gonder= web3_baglantisi.eth.send_raw_transaction(imzalanmis_mesaji_ayarla_islemi.rawTransaction)


mesaji_ayarla_islem_adisyonu = web3_baglantisi.eth.wait_for_transaction_receipt(mesaj_ayarla_islem_gonder) #reciept


print("devamdir versiyon 2", Merhaba_Dunya_TestNetteyiz.functions.mesajiSoyle().call())








