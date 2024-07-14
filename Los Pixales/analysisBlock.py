import pandas as pd
import re
import sys

# Check if the input file is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 analysis2Gematria.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Read the block numbers from the file
with open(input_file, 'r') as file:
    blocks = file.read().splitlines()

# Function to find repeating digits
def find_repeating_digits(blocks, digit, min_repeats):
    pattern = re.compile(f"({str(digit)}{{{min_repeats},}})")
    matching_blocks = [block for block in blocks if pattern.search(block)]
    count = len(matching_blocks)
    return matching_blocks, count

# Function to find palindromes
def find_palindromes(blocks, length):
    matching_blocks = [block for block in blocks if len(block) == length and block == block[::-1]]
    count = len(matching_blocks)
    return matching_blocks, count

# Function to find multiples
def find_multiples(blocks, multiple):
    matching_blocks = [block for block in blocks if int(block) % multiple == 0]
    count = len(matching_blocks)
    return matching_blocks, count

# Function to find 4 and 5 digit perfect squares
def find_perfect_squares(blocks):
    def is_perfect_square(n):
        root = int(n**0.5)
        return n == root * root

    matching_blocks = [block for block in blocks if (len(block) == 4 or len(block) == 5) and is_perfect_square(int(block))]
    count = len(matching_blocks)
    return matching_blocks, count

# Function to find blocks containing 420
def find_contains_420(blocks):
    matching_blocks = [block for block in blocks if '420' in block]
    count = len(matching_blocks)
    return matching_blocks, count

# Function to find powers of 7
def find_power_of_7(blocks):
    def is_power_of_7(n):
        if n <= 0:
            return False
        while n % 7 == 0:
            n //= 7
        return n == 1

    matching_blocks = [block for block in blocks if is_power_of_7(int(block))]
    count = len(matching_blocks)
    return matching_blocks, count

# Function to find Fibonacci numbers within blocks
def find_fibonacci(blocks, length):
    def generate_fibonacci(limit):
        fibs = [0, 1]
        while len(str(fibs[-1])) <= limit:
            fibs.append(fibs[-1] + fibs[-2])
        return fibs

    fib_numbers = set(str(num) for num in generate_fibonacci(length + 1) if len(str(num)) == length)
    matching_blocks = [block for block in blocks if any(fib in block for fib in fib_numbers)]
    count = len(matching_blocks)
    return matching_blocks, count

# Patterns to check
patterns = {
    '0': find_repeating_digits(blocks, '0', 1),
    '00': find_repeating_digits(blocks, '0', 2),
    '000': find_repeating_digits(blocks, '0', 3),
    '0000': find_repeating_digits(blocks, '0', 4),
    '00000': find_repeating_digits(blocks, '0', 5),
    '1': find_repeating_digits(blocks, '1', 1),
    '11': find_repeating_digits(blocks, '1', 2),
    '111': find_repeating_digits(blocks, '1', 3),
    '1111': find_repeating_digits(blocks, '1', 4),
    '11111': find_repeating_digits(blocks, '1', 5),
    '2': find_repeating_digits(blocks, '2', 1),
    '22': find_repeating_digits(blocks, '2', 2),
    '222': find_repeating_digits(blocks, '2', 3),
    '2222': find_repeating_digits(blocks, '2', 4),
    '22222': find_repeating_digits(blocks, '2', 5),
    '3': find_repeating_digits(blocks, '3', 1),
    '33': find_repeating_digits(blocks, '3', 2),
    '333': find_repeating_digits(blocks, '3', 3),
    '3333': find_repeating_digits(blocks, '3', 4),
    '33333': find_repeating_digits(blocks, '3', 5),
    '4': find_repeating_digits(blocks, '4', 1),
    '44': find_repeating_digits(blocks, '4', 2),
    '444': find_repeating_digits(blocks, '4', 3),
    '4444': find_repeating_digits(blocks, '4', 4),
    '44444': find_repeating_digits(blocks, '4', 5),
    '5': find_repeating_digits(blocks, '5', 1),
    '55': find_repeating_digits(blocks, '5', 2),
    '555': find_repeating_digits(blocks, '5', 3),
    '5555': find_repeating_digits(blocks, '5', 4),
    '55555': find_repeating_digits(blocks, '5', 5),
    '6': find_repeating_digits(blocks, '6', 1),
    '66': find_repeating_digits(blocks, '6', 2),
    '666': find_repeating_digits(blocks, '6', 3),
    '6666': find_repeating_digits(blocks, '6', 4),
    '66666': find_repeating_digits(blocks, '6', 5),
    '7': find_repeating_digits(blocks, '7', 1),
    '77': find_repeating_digits(blocks, '7', 2),
    '777': find_repeating_digits(blocks, '7', 3),
    '7777': find_repeating_digits(blocks, '7', 4),
    '77777': find_repeating_digits(blocks, '7', 5),
    '8': find_repeating_digits(blocks, '8', 1),
    '88': find_repeating_digits(blocks, '8', 2),
    '888': find_repeating_digits(blocks, '8', 3),
    '8888': find_repeating_digits(blocks, '8', 4),
    '88888': find_repeating_digits(blocks, '8', 5),
    '9': find_repeating_digits(blocks, '9', 1),
    '99': find_repeating_digits(blocks, '9', 2),
    '999': find_repeating_digits(blocks, '9', 3),
    '9999': find_repeating_digits(blocks, '9', 4),
    '99999': find_repeating_digits(blocks, '9', 5),
    'Palindrome 5': find_palindromes(blocks, 5),
    'Palindrome 6': find_palindromes(blocks, 6),
    'Multiples of 7': find_multiples(blocks, 7),
    'Multiples of 11': find_multiples(blocks, 11),
    'Multiples of 12': find_multiples(blocks, 12),
    'Multiples of 13': find_multiples(blocks, 13),
    'Multiples of 14': find_multiples(blocks, 14),
    'Multiples of 15': find_multiples(blocks, 15),
    'Multiples of 16': find_multiples(blocks, 16),
    'Multiples of 17': find_multiples(blocks, 17),
    'Multiples of 18': find_multiples(blocks, 18),
    'Multiples of 19': find_multiples(blocks, 19),
    'Multiples of 33': find_multiples(blocks, 33),
    'Multiples of 69': find_multiples(blocks, 69),
    'Contains 420': find_contains_420(blocks),
    'Power of 7': find_power_of_7(blocks),
    '3-digit Fibonacci': find_fibonacci(blocks, 3),
    '4-digit Fibonacci': find_fibonacci(blocks, 4),
    '5-digit Fibonacci': find_fibonacci(blocks, 5),
    '6-digit Fibonacci': find_fibonacci(blocks, 6)
}

# Convert the results to a DataFrame
summary = {key: value[1] for key, value in patterns.items()}
summary_df = pd.DataFrame(list(summary.items()), columns=['Pattern', 'Count'])

# Save the DataFrame to an Excel file
with pd.ExcelWriter('block_analysis_patterns.xlsx') as writer:
    summary_df.to_excel(writer, sheet_name='Summary', index=False)
    for pattern, (blocks, count) in patterns.items():
        df = pd.DataFrame(blocks, columns=[pattern])
        df.to_excel(writer, sheet_name=pattern, index=False)

print(summary_df)

