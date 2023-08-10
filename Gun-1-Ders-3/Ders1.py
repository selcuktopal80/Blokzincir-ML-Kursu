
#1) Bir network üzerindeki sözleşme ile etkileşim

from web3 import Web3 

# https://sepoliafaucet.com/

# https://dashboard.alchemy.com/

# https://sepolia.etherscan.io/address/0x5c894f4d2b7b0e116c1e4b3a1cab8c1a2a2f8a57#code


saglayici_url = "https://eth-sepolia.g.alchemy.com/v2/ywKo18csffAFR_LWA6zbg0ih4kAnQQ2l"

w3 = Web3(Web3.HTTPProvider(saglayici_url))


print(bool(w3.is_connected))

# sozlesme_abi= '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_receivers","type":"address[]"},{"name":"_value","type":"uint256"}],"name":"batchTransfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"payable":false,"stateMutability":"nonpayable","type":"fallback"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"previousOwner","type":"address"},{"indexed":true,"name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]'


# sozlesme_adresi= '0x5c894F4d2b7B0E116C1E4B3A1Cab8c1A2A2F8A57'

# sozlesme_ornegi= w3.eth.contract(address=sozlesme_adresi, abi=sozlesme_abi)

# token_supply= sozlesme_ornegi

# print(token_supply)

# print(w3.from_wei(token_supply, 'ether'))

# token_sembolu = sozlesme_ornegi.functions.symbol().call()

# print(token_sembolu)





#2) bir network'ün blockchain ve hesap bilgileri alma

son_blok_numarasi = w3.eth.block_number
print("son blok numarası : ", son_blok_numarasi)
print(w3.is_address('0x6e832874c7e22Eb8b9AA06d673A924EDC73F4E71'))
print(w3.is_address('0x8e8322874c72874c72874c72874c72874c72874c7'))
hesap_bakiyesi = w3.eth.get_balance('0x6e832874c7e22Eb8b9AA06d673A924EDC73F4E71')
print(hesap_bakiyesi)
print(w3.from_wei(hesap_bakiyesi, 'ether'))
print(w3.from_wei(1234567890123456789, 'ether'))