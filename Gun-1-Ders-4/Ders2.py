# pip install py-solc-x

# from solcx import compile_source

# compile_edilmis_solidity_kod = compile_source( '''

# // SPDX-License-Identifier: MIT

# pragma solidity ^0.8.0;

# contract MerhabaDunya {
    
#     string public mesaj;
    
#     constructor () {
        
#         mesaj = "Merhaba Dunya";
    
#     }
    
#     function mesajiAyarla(string memory _mesaj ) public {
        
#         mesaj = _mesaj;
#     }
    
#     function mesajiSoyle () view public returns (string memory) {
#         return mesaj;
#     }

# }
# ''', output_values=['abi','bin']
# )

# print(compile_edilmis_solidity_kod)

# sozlesme_id, sozlesme_arayuzu = compile_edilmis_solidity_kod.popitem()

# # print(sozlesme_id)

# print("abi : ", sozlesme_arayuzu['abi'])

# print("bin : ", sozlesme_arayuzu['bin'])


from solcx import compile_standard
import json
from web3 import Web3

#Sözleşme compile edip json dosyasini oluştururalım


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
print(compile_edilmis_sol)


with open("compile_edilmis_sol.json", "w") as file:
    json.dump(compile_edilmis_sol, file)

print("==============================================================")
#abi kodu alalım
MerhabaDunya_abi= compile_edilmis_sol["contracts"]["MerhabaDunya.sol"]["MerhabaDunya"]["abi"]
print(MerhabaDunya_abi)

#bytecodu alalım
MerhabaDunya_bytecode = compile_edilmis_sol["contracts"]["MerhabaDunya.sol"]["MerhabaDunya"]["evm"]["bytecode"]["object"]
print(MerhabaDunya_bytecode)