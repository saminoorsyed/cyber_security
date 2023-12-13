# Cryptographic hashes

1. what is weak-collsion resistance?
- Given an input to a hash functin it is computationally infeasible to find another input such that both inputs lead to the same hash output

2. what is strong-collision resistance?
- it is computationally infeasible to find two different inputs to a hash function that will lead to the same hash output

3. What is pre-image resistance?
- given an output of a hash function, it is computationally infeasible to find an input that will lead to the given output

4. the birthday paradox is related to which resistance?
- strong-collision resistance

5. for a cryptographic hash function with 160 bit output the probability of finding a colision reaches 50% after how many number of tries?
- 2^80. if there are 2^160 possible orientations, after trying 2^(m/2)

#Message authenticatin codes

DES is too small to work as a hash 2^56 possible keys

add key to keyless hash: MACk(m) = h(K|m|K) -> concatenate key to beginning and end of hash. reciever can try and compute the same hash to prove integrity

HMAC - sha512(k', m) = Sha512(k' xor [01011100]^8|SHa512(k' xor [00110110]^8||m))
Birthday attacks don't make sense because attackers dont't know key. including a key increases the space and makes a birthday attack harder

1. Can an adversary launch a birthday attack on HMAC?
- no becuase the adversary will not have the key to compute the hash
2. why do macs need to use a cryptoghraphic key?
- macs are crypto hashes sent along with a message. if they don't use a key, an adversary can modify the message and thekey and circumvent detection

# Pubic-Key Crypto intro

DSS = digital signature standard (for signatures only)

1. What are the two keys in public-key crypto called?
- public and private key

2. For preserving confidentiality using asymmetric-key or public-key crypto, which key should be used when encrypting?
- public-key

3. which publick-key systems can be used for both digital signatures and message encryption?
- RSA and Elliptic Curve

4. Public-key systems are computationally much more expensive than symmetric-key crypto?
- True

# Diffie-Hellman

Diffie-hellman = (common paint + secret paint)+ secret paint2 = shared secret pain 

1. what is the diffie-hellman public key system used for?
- key exchange

2. Diffie Hellman key exchange is suceptible to which of the following attacks?
- Man-in-the-middle

3. the security of Diffie-Hellman key exhange is based on what hard problem?
- computing dicrete logarithms in a large group

#RSA

1. what is RSA used for?
- Key exchange, digital signatures, message encryption

2. What hard problem is RSA based on?
- factoring large primes

# digital signatures

1. what is the value of using a hash in a digital signature?
- Both: allows detection of message tampering, reduces the cost of signatures as hash is typically much smaller

2. what properties do digital signatures provide?
- integrity, authenticity, non-repudiation
