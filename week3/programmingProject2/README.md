# Bloom Filter Readme

## Introduction
The provided Python script, `bloom_filter.py`, implements a Bloom filter, a space-efficient probabilistic data structure used for membership testing. The Bloom filter is loaded with values from the `rockyou.txt` file, and the script automates the testing of values from the `dictionary.txt` file. The script calculates and displays statistics, including true positive, true negative, false positive, and false negative values, based on the above files.

## Usage

### Prerequisites
- Python 3.x
- Ensure you have the `rockyou.txt` and `dictionary.txt` files available. These files should contain the values you want to load into the Bloom filter and test, respectively.

### Running the Script
You can run the Bloom filter script with the following command:

```bash
python bloom_filter.py input_file dictionary_file [--bits BITS] [--hashes HASHES]
```

here is an example command:

```bash
python3 bloom_filter.py rockyou.ISO-8859-1.txt dictionary.txt --bits 140000000 --hashes 3
```

- `input_file`: Path to the file containing values to populate the Bloom filter (e.g., `rockyou.txt`).
- `dictionary_file`: Path to the file containing values to be tested (e.g., `dictionary.txt`).
- `--bits`: (Optional) Number of bits in the Bloom filter. Default is `134190817`.
- `--hashes`: (Optional) Number of hash functions to use. Default is `3`.

### Output
The script will generate a `results.txt` file that contains the test results. This file lists each word from the `dictionary.txt` file and its corresponding test result (True Positive, True Negative, False Positive, or False Negative).

### Interpretation of Results
The script calculates and displays statistics in rounded percentages, based on the following definitions:

- `true_neg`: The percentage of words from dictionary.txt does not exist in `rockyou.txt` and were not identified by the Bloom filter.
- `false_neg`: The percentage of words from dictionary.txt exists in `rockyou.txt`, and were not identified by the Bloom filter.
- `false_pos`: The percentage of words from dictionary.txt is not in `rockyou.txt`, and were identified by the Bloom filter.
- `true_pos`: The percentage of words from dictionary.txt is in `rockyou.txt` and were identified by the Bloom filter.

The percentages are based on the total number of words tested and are displayed as rounded values. The script will also print these statistics to the console.

## Bloom Filter Implementation
The Bloom filter is implemented as a Python class named `BloomFilter`. It has the following methods:

- `__init__(self, bits: int, hash_count: int)`: Initializes the Bloom filter with the specified number of bits and the number of hash functions.
- `add_pwd(self, pwd: str)`: Adds a password to the Bloom filter by hashing it using each of the hash functions and setting the appropriate bit in the array.
- `check_pwd(self, pwd: str) -> bool`: Checks if a string is covered by the Bloom filter and returns `True` if the word is caught, or `False` if it is not caught.
- `get_words_in(self)`: Returns the number of words stored in the Bloom filter.
- `get_words_tested(self)`: Returns the number of words tested by the Bloom filter.
- `get_words_caught(self)`: Returns the number of words caught by the Bloom filter.
