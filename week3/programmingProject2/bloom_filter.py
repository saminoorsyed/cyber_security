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
                  "SHA-384", "SHA-512", "BLAKE2"]
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
        """
        given a string, this function checks if the string is covered by the bloom filter
        and returns False if the word is not caught and true if it is caught
        """
        self.words_tested += 1
        for hash_object in self.hash_objects[:self.hash_count]:
            new_hash_object = hash_object.copy()
            new_hash_object.update(pwd.encode('utf-8'))

            # find the bit to set in the bit array for the bloom filter
            hex_hashed = new_hash_object.hexdigest()
            integer_hash = int(hex_hashed, 16)
            bit_to_check = integer_hash % self.size

            if self.bit_array[bit_to_check] == 0:
                return False
        self.words_caught += 1
        return True

    def get_words_in(self):
        return self.words_in

    def get_words_tested(self):
        return self.words_tested

    def get_words_caught(self):
        return self.words_caught


def test_bloom_filter(bloom_instance: BloomFilter):
    """function to automate testing of bloom filer, reads in words from rockyou.txt and tests the words in dictionary.txt out puts a results.txt file and prints results to console"""
    # create a set of words from rockyou
    # add words to the bloom filter
    filter_set = set()
    try:
        with open("rockyou.ISO-8859-1.txt", 'r', encoding='ISO-8859-1') as fp:
            while True:
                line = fp.readline()
                if not line:
                    break
                filter_set.add(line)
                bloom_instance.add_pwd(line)
    except FileNotFoundError:
        print("input File not found.")
    except UnicodeDecodeError:
        print("Error decoding the input file")

    results = []
    results_dict = {
        'true_neg': 0,
        'false_neg': 0,
        'false_pos': 0,
        'true_pos': 0
    }

    try:
        with open("dictionary.txt", 'r', encoding='ISO-8859-1') as fp:
            while True:
                line = fp.readline()
                if not line:
                    break
                # if result returns true, then pwd is in the set of bad passwords
                result = bloom_instance.check_pwd(line)
                if result:
                    if line in filter_set:
                        # in the filter set and Id'ed as such
                        result_str = "True Positive"
                        results_dict['true_pos'] += 1
                    else:
                        # not in the filter set, but Id'ed as such
                        result_str = "False Positive"
                        results_dict['false_pos'] += 1
                else:
                    if line in filter_set:
                        # in the filter set, and not Id'ed as such
                        result_str = "False Negative"
                        results_dict['false_neg'] += 1
                    else:
                        # not in the filter set, and not Id'ed as such
                        result_str = "True Negative"
                        results_dict['true_neg'] += 1

                #  I would like to add the word tested to a file named "result.txt here"
                results.append(f"{line.strip()}: {result_str}\n")
    except FileNotFoundError:
        print("check File not found.")
    except UnicodeDecodeError as e:
        print(f"Error decoding the dictionary file: {e}")
    with open("./results.txt", 'w') as results_file:
        results_file.writelines(results)
    return results_dict


if __name__ == "__main__":
    # adjust the number of bits in the bit filter by changing the first arg, adjust the hashes by adjusting the second arg
    # you can choose between 1 and 8
    bloom_filter = BloomFilter(134190817, 3)
    results = test_bloom_filter(bloom_filter)

    true_neg = round (results['true_neg']/bloom_filter.words_tested *100)
    false_neg = round (results['false_neg']/bloom_filter.words_tested *100)
    false_pos = round (results['false_pos']/bloom_filter.words_tested *100)
    true_pos = round (results['true_pos']/bloom_filter.words_tested *100)

    print(f"the following results rounded percentages based on these definitions:\ntrue_neg = the word does not exists in rockyou.txt and was not Identified by the bloom filter\nfalse_neg = the word exists in rockyou.txt, but was not Identified by the bloom filter\nfalse_pos = the word is not in rockyou.txt but was Identified by the bloom filter\ntrue positive: the word is in the rockyou.txt and was identified by the bloom filter")
    print(
        f"the following are percentages based on the total number of words tested:\n true negative: {true_neg}%\n false negative: {false_neg}%\n false positive: {false_pos}%\n true positive: {true_pos}%")
