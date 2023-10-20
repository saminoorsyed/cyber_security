import random
import hashlib
import binascii

# define utility functions


def write_to_file(resultstr):
    with open("trials.txt", "a") as f:
        f.write(f"{resultstr}\n")


def generate_rand_bits(input_diversity: int) -> str:
    return str(random.getrandbits(input_diversity))


def hash_to_binary_string(hash_val: str, bits_to_check: int) -> str:
    bytes_hash = bytes.fromhex(hash_val)
    binary_string = binascii.hexlify(bytes_hash).decode('utf-8')
    return binary_string[2:bits_to_check]


def hash_string(input_string: str) -> str:
    # Create a hash of the input string using SHA-256
    hasher = hashlib.md5()
    hasher.update(input_string.encode('utf-8'))
    return hasher.hexdigest()


def weak_col_resistance(bits_to_check: int, input_diversity: int) -> int:
    """Function that checks the weak collision resistance property: finding a matching hash to a target hash"""
    trials = 0
    # set target hash and corresponding binary string
    target_input = generate_rand_bits(input_diversity)
    target_hash = hash(target_input)
    target_hash_bin_str = format(target_hash, 'b')[2:24]
    while True:
        input_val = generate_rand_bits(input_diversity)
        hashed_input = hash(input_val)
        hash_bin_str = format(hashed_input, 'b')[2:24]
        trials += 1
        if hash_bin_str == target_hash_bin_str:
            write_to_file(str(trials))
            return trials


def strong_col_resistance(bits_to_check: int, input_diversity: int) -> int:
    """Function that checks the strong collision property: finding any two hashes that match"""
    hash_set = set()
    trials = 0
    while True:
        input_val = generate_rand_bits(input_diversity)
        hashed_input = hash(input_val)
        hash_bin_str = format(hashed_input, 'b')[2:24]
        trials += 1
        if hash_bin_str in hash_set:
            write_to_file(str(trials))
            return trials
        hash_set.add(hash_bin_str)


# Experiment variables
num_experiments = 100
bits_checked = 24
input_div = 64

write_to_file("strong collision tests \n")
# Perform experiments for strong collision property
strong_collision_trials = [strong_col_resistance(bits_checked, input_div)
                           for _ in range(num_experiments)]
average_strong_collision_trials = sum(
    strong_collision_trials) / num_experiments

# Perform experiments for weak collision resistance
write_to_file("weak collision tests \n")
weak_collision_trials = [weak_col_resistance(
    bits_checked, input_div) for _ in range(num_experiments)]
average_weak_collision_trials = sum(weak_collision_trials) / num_experiments

# Print results
print(
    f"Average trials to break weak collision resistance property: {average_weak_collision_trials}")
print(
    f"Average trials to break strong collision property: {average_strong_collision_trials}")

if average_weak_collision_trials < average_strong_collision_trials:
    print("Weak collision resistance property is easier to break using brute-force.")
else:
    print("strong collision property is easier to break using brute-force.")
