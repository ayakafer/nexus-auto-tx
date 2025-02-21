import os
import time
import random
from web3 import Web3

# Konfigurasi RPC Nexus
NEXUS_RPC = "https://rpc.nexus.xyz"
CHAIN_ID = 392
web3 = Web3(Web3.HTTPProvider(NEXUS_RPC))

# Private keys dan akun
PRIVATE_KEY_1 = "isi dengan private key kalian"
PRIVATE_KEY_2 = "isi dengan private key kalian"

ACCOUNT_1 = web3.eth.account.from_key(PRIVATE_KEY_1).address
ACCOUNT_2 = web3.eth.account.from_key(PRIVATE_KEY_2).address

# Fungsi untuk mengirim native token
def transfer_native_token(sender_private_key, recipient_address, amount):
    sender_account = web3.eth.account.from_key(sender_private_key)
    nonce = web3.eth.get_transaction_count(sender_account.address)
    
    transaction = {
        'to': recipient_address,
        'value': web3.to_wei(amount, 'ether'),
        'gas': 21000,
        'gasPrice': web3.eth.gas_price,
        'nonce': nonce,
        'chainId': CHAIN_ID
    }
    
    signed_txn = web3.eth.account.sign_transaction(transaction, sender_private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
    print(f"Transaction sent: https://explorer.nexus.xyz/tx/{tx_hash.hex()}")
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transaction confirmed.")

# Fungsi utama untuk transaksi bergantian
def start_transaction_loop():
    while True:
        random_amount_1 = round(random.uniform(1, 10), 2)  # Random 1-10 NX
        print(f"Wallet 1 sending {random_amount_1} NX to Wallet 2...")
        transfer_native_token(PRIVATE_KEY_1, ACCOUNT_2, random_amount_1)
        time.sleep(900)  # Tunggu 15 menit

        random_amount_2 = round(random.uniform(1, 10), 2)  # Random 1-10 NX
        print(f"Wallet 2 sending {random_amount_2} NX to Wallet 1...")
        transfer_native_token(PRIVATE_KEY_2, ACCOUNT_1, random_amount_2)
        time.sleep(900)  # Tunggu 15 menit

if __name__ == "__main__":
    print("Starting transaction loop...")
    start_transaction_loop()