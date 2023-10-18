import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as pad

def main():
    parser = argparse.ArgumentParser(description="finds the cryptographic key based on the words.txt, plain.txt, and cipher.txt")
    parser.add_argument("plaintext", help="provide the plaintext as a hexadecimal string", type=str)
    parser.add_argument("ciphertext", help="provide the cipher hex string as a hexadecimal string", type=str)

    args = parser.parse_args()
    plaintext = args.plaintext.encode('utf-8')  # Convert hex string to bytes
    ciphertext = bytes.fromhex(args.ciphertext)  # Convert hex string to bytes

    if not plaintext or not ciphertext:
        print("missing either plaintext or ciphertext, please provide them")
        return

    with open('words.txt') as file:
        word_list = [line.strip() for line in file]

    # Define IV outside of for loop as 16 bytes of 0
    iv = b'\x00' * 16
    print(plaintext[:21])
    for word in word_list:
        if len(word) >= 16:
            continue
        padding_str = ' ' * (16 - len(word))
        key = (word + padding_str)

        cipher = Cipher(algorithms.AES(key.encode('utf-8')), modes.CBC(iv))

        # Decrypt the ciphertext and match it with the plaintext
        decryptor = cipher.decryptor()
        decryption = decryptor.update(ciphertext) + decryptor.finalize()
        if decryption[:21] == plaintext:
            print(f"key: {word}")
            print(f"decrypted text: {decryption}")
            print(f"plaintext     : {plaintext}")  # Convert bytes back to hex for printing

if __name__ == "__main__":
    main()
