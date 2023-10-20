# Hash Collision Resistance Tester

This Python script is designed to test the collision resistance of cryptographic hash functions, specifically the **weak collision resistance** and **strong collision resistance** properties. It generates random input values, hashes them using the pythons built in hash function, and checks for collisions (matching hash values). The script provides detailed information about the number of trials required to break these properties.

## Prerequisites

Before using this script, make sure you have Python installed on your system. This script is written in Python 3.

## How to Use

Follow these steps to use the script:

1. Clone or download the script to your local machine.

2. Open your terminal or command prompt.

3. Navigate to the directory where the script is located.

4. Run the script using the following command:

   ```bash
   python pre-image_resistance.py
   ```

5. The script will execute a series of experiments to test the collision resistance properties. The results will be displayed in the terminal, and the details will be saved to a file called `trials.txt` in the same directory as the script. 

## Script Functions

The script contains the following functions:

### `write_to_file(resultstr)`

- This function appends a string `resultstr` to a file named `trials.txt`.

### `generate_rand_bits(input_diversity: int) -> str`

- Generates random bits as a string, using the Python `random` library.

### `weak_col_resistance(bits_to_check: int, input_diversity: int) -> int`

- Checks the **weak collision resistance property** by attempting to find a matching hash to a target hash. The number of trials required to find a collision is returned.

### `strong_col_resistance(bits_to_check: int, input_diversity: int) -> int`

- Checks the **strong collision property** by attempting to find any two hashes that match. The number of trials required to find a collision is returned.

## Experiment Variables

The script allows you to customize the following experiment variables:

- `num_experiments`: The number of experiments to run for each collision resistance property. Default is 100.

- `bits_checked`: The number of bits to check when comparing hash values. Default is 24.

- `input_div`: The input diversity, which defines the number of random bits to generate for the input values. Default is 64.

## Results

After running the experiments, the script prints the following information:

- Average trials to break **weak collision resistance** property.

- Average trials to break **strong collision property**.

- A conclusion regarding which property is easier to break using brute-force.

## Notes

This script uses pythons hash function which is based on the sipHash algorithm. it is thought to be cryptographically secure. 

Please be cautious when running this script, as it involves random experiments and may take some time to complete. The results are recorded in the `trials.txt` file for your reference. When running it on my own computer took about 10 minutes to run

There is an included document labeled `example_trials.txt` with a set of trials that I obtained from running this script before I turned it in. 

## Sources

source:https://andrewbrookins.com/technology/pythons-default-hash-algorithm/
source:https://docs.kernel.org/security/siphash.html#:~:text=Security,2%5E128%20outputs%20is%20significant. 