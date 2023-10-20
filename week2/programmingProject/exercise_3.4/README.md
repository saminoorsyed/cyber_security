## Exercise 3.4 directions
# Directions:

1) unzip the repository into it's own directory
2) that directory should have three files:
    a) brute_force.py
    b) words.txt
    c) README.md
3) cd into the directory with the files and run the following command:

python3 brute_force.py 'This is a top secret.' '8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9'

Notes: 
1) the first argument is the plaintext, the second is the ciphertext. 
2) The relative location of words.txt is hard coded into the program, so it is essential that it be in the same directory that you are in when you run the program
3) this script uses the cryptography package that comes with python and makes use of openssl.


Sources:
https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/