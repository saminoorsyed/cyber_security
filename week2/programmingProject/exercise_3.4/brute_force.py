# what do we know:
# aes-128-cbc
# IV = 000000...
# key = english word shorter than 16 characters with spaces at the end to pad


import argparse
from cryptography import Cipher, algorithms, modes


def main():
    parser = argparse.ArgumentParser(description="finds the cryptographic key based on the words.txt, plain.txt and cipher.txt")
    parser.add_argument("plaintext", help= "provide the plaintext as a string arg", type= str)
    parser.add_argument("ciphertext", help="provide the cipher hex string as a string argument", type=str)

    args = parser.parse_args()
    plaintext = args.plaintext
    ciphertext = args.ciphertext

    if not plaintext or not ciphertext:
        print("missing either plaintext or ciphertext, please provide them")
        return
    
    with open('words.txt')as file:
        word_list = [line.strip() for line in file]
    
    # define IV outside of for loop as a 16 bytes of 0
    iv = b'\x00'*16

    for word in word_list:
        padding = ' '*(16-len(word))
        key = word+padding
        # default is aes 128
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

        # decrypt the cipher text and match it with the plaintext
        decryptor = cipher.decryptor()
        decryption = decryptor.update(ciphertext)

        if decryption == plaintext:
            print(f"key: {word}")
            print(f"decrypted text: {decryption}")
            print(f"plaintext     : {plaintext}")
