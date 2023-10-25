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
    def __init__(self, bits: int, hash_count: int):
        # use this for modulo arithmitic when adding to the bloom filter or checking
        self.size = bits
        # this is the actual bloom filter
        self.bit_array = array('b', [0]*bits)
        # avalable hashes from hashlib library
        hashes = ["MD5", "SHA-1", "SHA-224", "SHA-256",
                       "SHA-384", "SHA-512"]
        # number of hashes, k
        self.hash_count = hash_count
        # create a list of hash objects for later use
        self.hash_objects = []
        for hash in hashes[:self.hash_count]:
            hash_object = hashlib.new(hash)
            self.hash_objects.append(hash_object)
        # track the number of words stored in the bloom filter
        self.words_in = 0
        # track the words tested by the bloom filter
        self.words_tested = 0
        # track the words caught by the bloom filter
        self.words_caught = 0

    def add_pwd(self, pwd: str):
        """ adds a password to the bloom filter by hashing it using each of the hash functions and setting the appropriate bit in the array"""
        self.words_in += 1

        for hash_object in self.hash_objects[:self.hash_count]:
            # need to clone the hash object to do a fresh hash on each word
            # repeated calls to the same hash object would result in a hash of a+b+c
            new_hash_object = hash_object.copy()
            new_hash_object.update(pwd.encode('utf-8'))

            # find the bit to set in the bit array for the bloom filter
            hex_hashed = new_hash_object.hexdigest()
            integer_hash = int(hex_hashed, 16)
            bit_to_set = integer_hash % self.size
            self.bit_array[bit_to_set] = 1

    def check_pwd(self, pwd: str) -> bool:
        self.words_tested += 1
        for hash_object in self.hash_objects[:self.hash_count]:
            new_hash_object = hash_object.copy()
            new_hash_object.update(pwd.encode('utf-8'))

            # find the bit to set in the bit array for the bloom filter
            hex_hashed = new_hash_object.hexdigest()
            integer_hash = int(hex_hashed, 16)
            bit_to_check = integer_hash % self.size

            if self.bit_array[bit_to_check] == 0:
                self.words_caught += 1
                return False

        return True

    def get_words_in(self):
        return self.words_in

    def get_words_tested(self):
        return self.words_tested

    def get_words_caught(self):
        return self.words_caught


def test_bloom_filter(bloom_instance: BloomFilter):
    """function to automate testing of bloom filer, reads in words from rockyou.txt and tests the words in dictionary.txt out puts a results.txt file and prints results to console"""
    # add words to the bloom filter
    try:
        with open("./rockyou.ISO-8859-1.txt", 'r', encoding='ISO-8859-1') as fp:
            while True:
                line = fp.readline()
                if not line:
                    break
                bloom_instance.add_pwd(line)
    except FileNotFoundError:
        print("input File not found.")
    except UnicodeDecodeError:
        print("Error decoding the input file")

    results = []

    try:
        count = 0
        with open("./dictionary.txt", 'r') as fp:
            while True:
                line = fp.readline()
                count += 1
                if not line:
                    break
                result = bloom_instance.check_pwd(line)
                #  I would like to add the word tested to a file named "result.txt here"
                results.append(f"{line.strip()}: {result}\n")
    except FileNotFoundError:
        print("check File not found.")
    except UnicodeDecodeError:
        print("Error decoding the check file")
    print(count)
    with open("./results.txt", 'w') as results_file:
        results_file.writelines(results)


if __name__ == "__main__":
    # adjust the number of bits in the bit filter by changing the first arg, adjust the hashes by adjusting the second arg
    # you can choose between 1 and 6
    bloom_filter = BloomFilter(134190817, 4)
    test_bloom_filter(bloom_filter)
    print(f"words loaded into the bloom filter: {bloom_filter.get_words_in()} \n words caught by the bloom filter: {bloom_filter.get_words_caught()} \n words tested:{bloom_filter.get_words_tested()}")
