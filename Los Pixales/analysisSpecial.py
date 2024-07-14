import pandas as pd
import sys

# Check if the input file is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 analysis2Gematria.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Read the block numbers from the file
with open(input_file, 'r') as file:
    blocks = file.read().splitlines()

# Convert block numbers to integers
blocks = [int(block) for block in blocks]

# Function to generate Fibonacci numbers up to a certain limit
def generate_fibonacci(limit):
    fibs = [0, 1]
    while fibs[-1] <= limit:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:-1]  # Exclude the last number that exceeds the limit

# Function to generate powers of 7 up to a certain limit
def generate_powers_of_7(limit):
    powers = []
    n = 1
    while n <= limit:
        powers.append(n)
        n *= 7
    return powers

# Determine the maximum block number to set a limit for Fibonacci and powers of 7 generation
max_block = max(blocks)

# Generate Fibonacci numbers and powers of 7
fibonacci_numbers = generate_fibonacci(max_block)
powers_of_7 = generate_powers_of_7(max_block)

# Print the generated sequences for verification
print("Generated Fibonacci numbers up to max block:", fibonacci_numbers)
print("Generated powers of 7 up to max block:", powers_of_7)

# Find block numbers that are Fibonacci numbers
fib_blocks = [block for block in blocks if block in fibonacci_numbers]

# Find block numbers that are powers of 7
power_of_7_blocks = [block for block in blocks if block in powers_of_7]

print("Fibonacci block numbers:", fib_blocks)
print("Power of 7 block numbers:", power_of_7_blocks)

# Check each block n
