# What is cryptogrophy?

cryptography = secret writing

1. what security property/ attribute do crypto hashes support?
	- Integrity
2. what security property/ attribute do digital signatures support?
	- integrity. send a hash of the info along with msg
	- accountability
	- authenticity
what security property/ attribute does encryption support?
	- Confidentiality
	- privacy
What security property/ attribute do message authentication codes support?
	- Integrity

# What is Encryption

What are the two types of encryption?
	- symmetric and asymmetric encryption
Which is older?
	- Symmetric
Public Key encryption?
	- Alice distributes a public Key and keeps her private key.
	- only she can read messages that are sent to her.
What security principle exemplifies kerchoffs principle?
	- open design
	- attacker knows the algo, but not the secret key
What are the four types of attacks on ciphers?
	- cipher text only
	- known plain text (and cipher text) try to find key
	- chosen plain text (access to an encryption oracle)
	- chosen cipher text ( access to both encryption and decryption oracle)
Typically attacks are based on:
1. some weakness on the underlying mathematics
2. Statistical attacks (models of the language)

# Classical Cyphers

1. Which of the following is a well known classical cipher?
	-Caeser
2. What are two basic types of classical ciphers?
	- Substitution and transposition
	- Caesar is substitution
	- rail cipher is transposition

3. What is the key in the rail-fence cipher?
	- the number of columns the message is cut into
4. which cipher is proven unbeatable?
	-one-time pad
# Modern Ciphers

Current good security = 2^80 or 10^24, 2^128, 10^34 is even better, 

## Block Cipher
- Ek(b1)Ek(b2)... use the same encryption on blocks of info
- stream vipher = k1k2k3...
	- Ek(m) =Ek1(b1)Ek2(b2)...
	- if k1k2... repeats, cipher period is one cycle of k1k2...
## Current encryption standard
until 2001:
	- block cipher of 64 bits using a 56 bit key
	- outputs 64 bits of ciphertext
Since 2001:
	- Block-cipher
	- encrypts blocks of 128 bits using keys of 128/196/256 bits
	- outputs 128 bits of cipher text
Avalanch effect:
	- a change in one input or key bit results in a 50% change of output bits
## DES
- considered weak always
- diffie hellman said in 1999 that it would be cracked
- was originally not available to the public
### How to brute force it
- known plaintext needed (you have a PT and CT) just go through possible keys
	-2^56 possible keys
	- statistical models can help
	- how do we reduce the amount of work
### double DES
Encode it twice Ek2(Ek1(P)
subject to *meet* in the middle and there for it's onl 2^n+1
decrypt the pt and encrypt the ct to find when they match in the middle
### triple DES
protects againts meet in the middle attack
middle operation is inverse of 1st and 3rd k
C = DESk(DESk'^-1(DESk"(m)))
expected 168 bit security, but ends up being only 80 bit security
	-meet in the middle twice 112 bit
backwards compatibal with DES (all keys the same)
## AES
- symmetric block cipher 128/192/256 block cipher
- stronger and faster than triple DES
- active life of 20+ years (archival)
- full specification and design details made available

MODERN CIPHERS ARE ALL PRODUCT CIPHERS (block and stream)
AES is current encryption standard and work horse
both double and tripple DES are susceptible to meet in th middle attack

##Encryption modes

ECB- Electronic code book (each block is encrypted) reveals shape of data
OFB- output feedback mode  apply the block cipher on init vector and then xor with message to get cipher text
	- encrypted iv become init vector for next. makes a block cipher look like a stream cipher
	- no reverse of encryption to decrypt just find all the init vectors from original and apply to cipher text with xor operation
Counter Mode - Ek(counter1)+m1 = c1, EK(counter2)+m2 = c2...
	- also converts a block cipher to a stream cipher
	- can be done in parallel all you need is the counter value

identify the following mode: k(m0initial vector) (+ = xor) = c0, k(m1+c0) = c1...
	- init vector xor with message before encryption xor then encrypt
	- ciphertext is init vector for the next encryption
	- CBC= cipher block chaining
	- to decrypt, use the same process in reverse
What is an Encryption mode?
- a way for block ciphers to encrypt messages larger than the block size

WHich of the following modes has a self healing property?
- CBC- error only propogates for two blocks
which of the following modes convers a block cipher into a stream cipher?
- OFB and CTR
which of the following modes is parallelixable?
- CTR
