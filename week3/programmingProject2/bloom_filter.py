'''The software will implement a Bloom filter.
Bloom filter will be loaded with values from rockyou.txt.
The software will automate the testing of values in dictionary.txt.
The software will calculate and display statistics on true positive, true negative, false positive, and false negative for the dictionary.txt based on the rockyou.txt.'''

# imports
import hashlib
from array import array

# Create a bit array
# bit_array = array('b', [0, 1, 0, 1, 1, 0, 0, 1])


class BloomFilter:
    def __init__(self, bits: int, hashes: list):
        # use this for modulo arithmitic when adding to the bloom filter or checking
        self.size = bits
        # this is the actual bloom filter
        self.bit_array = array('b', [0]*bits)
        # number of hashes, k
        self.hash_count = len(hashes)
        # create a list of hash objects for later use
        self.hash_objects = []
        for hash in hashes:
            hash_object = hashlib.new(hash)
            self.hash_objects.append(hash_object)

    def add_pwd(self, pwd: string):
        """ adds a password to the bloom filter by hashing it using each of the hash functions and setting the appropriate bit in the array"""
        for hash_object in self.hash_objects:
            # need to clone the hash object to do a fresh hash on each word
            # repeated calls to the same hash object would result in a hash of a+b+c
            new_hash_object = hash_object.copy()
            new_hash_object.update(pwd.encode('utf-8'))

            # find the bit to set in the bit array for the bloom filter
            hex_hashed = new_hash_object.hexdigest()
            integer_hash = int(hex_hashed, 16)
            bit_to_set = integer_hash % self.size
            self.bit_array[bit_to_set] = 1
    
    def check_pwd(self, pwd:string)-> bool:
        for hash_object in self.hash_objects:
            new_hash_object = hash_object.copy()
            new_hash_object.update(pwd.encode('utf-8'))

            # find the bit to set in the bit array for the bloom filter
            hex_hashed = new_hash_object.hexdigest()
            integer_hash = int(hex_hashed, 16)
            bit_to_check = integer_hash % self.size

            if self.bit_array[bit_to_check] == 0:
                return False
                
        return True
            