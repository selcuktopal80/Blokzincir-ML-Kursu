
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3



import os
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy




def generate_account():

    
    mnemonic = os.getenv("MNEMONIC")

    
    wallet = Wallet(mnemonic)

    
    private, public = wallet.derive_account("eth")

    
    account = Account.from_key(private)

    return account

def get_balance(w3, address):
  
    
    wei_balance = w3.eth.get_balance(address)

    
    ether = w3.from_wei(wei_balance, "ether")

    
    return ether


def send_transaction(w3, account, to, wage):
    
    
    w3.eth.set_gas_price_strategy(medium_gas_price_strategy)

    
    value = w3.to_wei(wage, "ether")

    
    gasEstimate = w3.eth.estimate_gas({"to": to, "from": account.address, "value": value})

    
    raw_tx = {
        "to": to,
        "from": account.address,
        "value": value,
        "gas": gasEstimate,
        "gasPrice": 875000000,
        "nonce": w3.eth.get_transaction_count(account.address)
    }

    
    signed_tx = account.signTransaction(raw_tx)

    
    return w3.eth.send_raw_transaction(signed_tx.rawTransaction)

w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
print(w3.is_connected())



candidate_database = {
    
    "Fikri": ["Fikri", w3.eth.accounts[4], "1.1", .80, "Images/oturevinde.jpeg"],
    "Elon": ["Elon", w3.eth.accounts[5], "3.5", .33, "Images/elon.jpeg"],
    "Trump": ["Trump", w3.eth.accounts[6], "1.7", .19, "Images/trump.jpeg"],
    "Vitalik": ["Vitalik", w3.eth.accounts[7], "5", .95, "Images/vitalik.jpeg"]
}


people = ["Fikri", "Elon", "Trump", "Vitalik"]



db_list = list(candidate_database.values())

for number in range(len(people)):
    st.image(db_list[number][4], width=200)
    st.write("Isim: ", db_list[number][0])
    st.write("Ethereum Hesap Adresi: ", db_list[number][1])
    st.write("Başına İş Aç Com Puanlamaları: ", db_list[number][2])
    st.write("Ether Basina Saatlik Ucret: ", db_list[number][3], "eth")
    st.text(" \n")

################################################################################
# Streamlit Uygulama Kodu
################################################################################



st.sidebar.markdown("## Müşteri Hesabı Adresi ve Ether Cinsinden Ethereum Bakiyesi")

##########################################
#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################
# Step 1 - Part 5:
# Call `get_balance` function and pass it your account address
ether = get_balance(w3, account.address)
# Write the returned ether balance to the sidebar
st.sidebar.write(ether)
##########################################
# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Seç Bir Bela', people)
# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Saat Sayısı")
st.sidebar.markdown("## Aday Adı, Saatlik Ücret ve Ethereum Adresi")
# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]
# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(candidate)
# Identify the FinTech Finder candidate's hourly rate
hourly_rate = candidate_database[person][3]
# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)
# Identify the FinTech Finder candidate's Ethereum Address
candidate_address = candidate_database[person][1]
# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)
# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.markdown("## Ether cinsinden Toplam Ücret")

################################################################################
# Step 2: Sign and Execute a Payment Transaction
##########################################
# Step 2 - Part 1:
# * Write the equation that calculates the candidate’s wage. 
wage =  hourly_rate * hours

# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(wage)

##########################################
# Step 2 - Part 2:
# * Call the `send_transaction` function 
if st.sidebar.button("İşlem Gönder (Ödeme Yap)"):    
    transaction_hash = send_transaction(w3,account, candidate_address, wage)
    # Markdown for the transaction hash
    st.sidebar.markdown("#### Doğrulanmış İşlem Hash'i")

    # Write the returned transaction hash to the screen
    st.sidebar.text(transaction_hash.hex())

    # Celebrate your successful payment
    st.balloons()


# The function that starts the Streamlit application


