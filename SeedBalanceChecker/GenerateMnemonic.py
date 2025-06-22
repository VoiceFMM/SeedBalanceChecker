import hashlib
import random
import os
import sys

path = os.path.dirname(os.path.abspath(__file__)) # Додає зміну path, для пошуку та запису у файли
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    # Функція, яка генерує seed разу
def generate_random_mnemonic():

    # Функція, яка завантажує список з 2048 слів
    # які використовуються для створення seed фрази
    def load_wordlist():
       
        with open(f"{path}\\data\\english.txt", "r", encoding="utf-8") as f:
            return [word.strip() for word in f.readlines()]
    
    #Функція, яка первіряє чи являються 12 рандомних слів з 2048 - seed фразою 
    def is_valid_mnemonic(mnemonic_words, wordlist):
        if len(mnemonic_words) != 12:
            return False
        try:
            indexes = [wordlist.index(word) for word in mnemonic_words]
        except ValueError:
            return False

        bits = ''.join(bin(index)[2:].zfill(11) for index in indexes)
        entropy_bits = bits[:128]
        checksum_bits = bits[128:]

        entropy_bytes = int(entropy_bits, 2).to_bytes(16, byteorder="big")
        hash_bytes = hashlib.sha256(entropy_bytes).digest()
        hash_bits = bin(int.from_bytes(hash_bytes, byteorder="big"))[2:].zfill(256)
        actual_checksum = hash_bits[:4]

        return checksum_bits == actual_checksum


    #Тіло функції
    while True:
        wordlist = load_wordlist() #Завантаження списку з 2048 слів
        words = random.choices(wordlist, k=12) # Вибір 12 рандомних слів з 2048
        if is_valid_mnemonic(words, wordlist): #Перевірка чи являються ці слова - seed фразою
            return words #Повернення функції (повертає валідну seed фразу)
     


