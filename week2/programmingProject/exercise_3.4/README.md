# Exercise 3.4 - Cryptographic Key Finder

This Python script is designed to find the cryptographic key based on provided plaintext and ciphertext. It makes use of the `cryptography` package in Python, which relies on the `openssl` library.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Notes](#notes)
- [Sources](#sources)

## Installation

1. Unzip the repository into its own directory. Ensure that the directory contains the following three files:

    a) `brute_force.py`
    b) `words.txt`
    c) `README.md`

2. Open your terminal or command prompt.

3. Navigate to the directory with the files.

## Usage

Execute the script by running the following command:

```bash
python3 brute_force.py 'This is a top secret.' '8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9'
```

### Arguments

1. The first argument is the plaintext provided in hexadecimal format.
2. The second argument is the ciphertext provided in hexadecimal format.

**Note:** The relative location of `words.txt` is hard-coded into the program, so it is essential that it be in the same directory where you run the program.

### Output

The script reads from the `words.txt` file and attempts to find the cryptographic key. Once the key is found, it will display:

- The key.
- The decrypted text.
- The original plaintext.

## Notes

1. Ensure that you have both the plaintext and ciphertext arguments in hexadecimal format when running the script.

2. The script utilizes the `cryptography` package, which relies on `openssl`. Make sure you have the necessary dependencies installed.

## Sources

- [Cryptography - Hazmat Primitives Symmetric Encryption](https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/)

---

**Please exercise caution when running this script.** The results may take some time, depending on the complexity of the key. This script is intended for educational purposes to understand cryptographic concepts.