from eth_account import Account
from eth_keys import keys
import os
import sys

path = os.path.dirname(os.path.abspath(__file__)) # Додає зміну path, для пошуку та запису у файли
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

Account.enable_unaudited_hdwallet_features() # Вмикаємо роботу з HD-wallet

def PrivPublKeysAdr(mnemonic_phrase: list, numb:int = 1):
    if type(mnemonic_phrase) == list:
        mnemonic_phrase = " ".join(mnemonic_phrase)
    AdrLst = []
        
    for i in range(numb):
        # Шлях derivation: стандартний шлях для Ethereum (BIP-44)
        account_path = f"m/44'/60'/0'/0/{i}"

        # Генерація аккаунту з фрази
        account = Account.from_mnemonic(mnemonic_phrase, account_path=account_path)

        # Отримуємо дані
        private_key_hex = account.key.hex()
        address = account.address

       
        priv_key_obj = keys.PrivateKey(account.key)
        public_key_hex = priv_key_obj.public_key.to_hex()

        AdrLst.append([address, private_key_hex, public_key_hex, mnemonic_phrase, i])
            
    return AdrLst
            

