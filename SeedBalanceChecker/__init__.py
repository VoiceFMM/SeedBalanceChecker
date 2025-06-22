import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from GenerateMnemonic import generate_random_mnemonic
from GeneratePrivPublKeysAdr import PrivPublKeysAdr
from CheckBalances import ChecBalance

def main(number):
    while True:
        mnemonicPhrase = generate_random_mnemonic()
        Adrs = PrivPublKeysAdr(mnemonicPhrase,numb=number)
        if ChecBalance(Adrs):
            print("FIND")
            break
        

