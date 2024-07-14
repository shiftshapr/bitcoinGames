import pandas as pd
import re
import sys
import math
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Check if the input file is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 analysisBlock.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Read the block numbers from the file
with open(input_file, 'r') as file:
    blocks = file.read().splitlines()

# Strip newlines and convert to strings
block_numbers = [num.strip() for num in blocks]

# Function to check if a number is a perfect square
def is_perfect_square(n):
    root = math.isqrt(n)
    return n == root * root

# Function to find all 3, 4, 5, or 6-digit perfect squares within a block number
def find_embedded_perfect_squares(block, digit_length):
    embedded_squares = []
    block_str = str(block)
    
    for i in range(len(block_str) - digit_length + 1):
        substring = block_str[i:i+digit_length]
        if len(substring) == digit_length and substring[0] != '0':
            num = int(substring)
            if is_perfect_square(num):
                embedded_squares.append(num)
    
    return embedded_squares

# Function to find repeating digits
def find_repeating_digits(blocks, digit, exact_repeats):
    pattern = re.compile(fr"(\d*?{digit}{{{exact_repeats}}})")
    matching_blocks = [block for block in blocks if pattern.search(block)]
    count = len(matching_blocks)
    logging.debug(f"Found {count} blocks matching pattern {pattern.pattern} for {digit} repeated {exact_repeats} times")
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

def find_contains(blocks, number):
    matching_blocks = [block for block in blocks if str(number) in block]
    count = len(matching_blocks)
    return matching_blocks, count

# Function to find powers of 7
def find_power_of_7(blocks):
    powers_of_7 = {length: [] for length in range(3, 7)}
    powers_of_7_counts = {length: 0 for length in range(3, 7)}

    for block in blocks:
        block_str = str(block)
        for length in range(3, 7):
            for i in range(len(block_str) - length + 1):
                substring = block_str[i:i+length]
                if substring.isdigit() and len(substring) == length and int(substring) >= 10**(length-1) and is_power_of_7(int(substring)):
                    powers_of_7[length].append(block)
                    powers_of_7_counts[length] += 1
                    print(f"Matching substring found: {substring} in block {block}")

    return powers_of_7, powers_of_7_counts

def is_power_of_7(n):
    if n == 0:
        return False
    n_str = str(n)
    power = 0
    temp = int(n_str)
    while temp % 7 == 0:
        temp //= 7
        power += 1
    return temp == 1

# Call the find_power_of_7 function and store the result
powers_of_7, powers_of_7_counts = find_power_of_7(block_numbers)


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

# Function to calculate 1-digit gematria number
def calculate_gematria(block, single_digit=True):
    sum_digits = sum(int(digit) for digit in block)
    if single_digit:
        while sum_digits >= 10:
            sum_digits = sum(int(digit) for digit in str(sum_digits))
    return sum_digits

# Function to count digits in each position from the end
def count_digits_in_positions(numbers):
    max_length = max(len(num) for num in numbers)
    digit_counts = {f"D{i}": {str(d): 0 for d in range(10)} for i in range(max_length)}

    for num in numbers:
        reversed_num = num[::-1]  # Reverse the number to start counting from the end
        for i, digit in enumerate(reversed_num):
            digit_counts[f"D{i}"][digit] += 1

    return digit_counts

# Patterns to check
patterns = {
    '0': find_repeating_digits(block_numbers, '0', 1),
    '00': find_repeating_digits(block_numbers, '0', 2),
    '000': find_repeating_digits(block_numbers, '0', 3),
    '0000': find_repeating_digits(block_numbers, '0', 4),
    '00000': find_repeating_digits(block_numbers, '0', 5),
    '1': find_repeating_digits(block_numbers, '1', 1),
    '11': find_repeating_digits(block_numbers, '1', 2),
    '111': find_repeating_digits(block_numbers, '1', 3),
    '1111': find_repeating_digits(block_numbers, '1', 4),
    '11111': find_repeating_digits(block_numbers, '1', 5),
    '2': find_repeating_digits(block_numbers, '2', 1),
    '22': find_repeating_digits(block_numbers, '2', 2),
    '222': find_repeating_digits(block_numbers, '2', 3),
    '2222': find_repeating_digits(block_numbers, '2', 4),
    '22222': find_repeating_digits(block_numbers, '2', 5),
    '3': find_repeating_digits(block_numbers, '3', 1),
    '33': find_repeating_digits(block_numbers, '3', 2),
    '333': find_repeating_digits(block_numbers, '3', 3),
    '3333': find_repeating_digits(block_numbers, '3', 4),
    '33333': find_repeating_digits(block_numbers, '3', 5),
    '4': find_repeating_digits(block_numbers, '4', 1),
    '44': find_repeating_digits(block_numbers, '4', 2),
    '444': find_repeating_digits(block_numbers, '4', 3),
    '4444': find_repeating_digits(block_numbers, '4', 4),
    '44444': find_repeating_digits(block_numbers, '4', 5),
    '5': find_repeating_digits(block_numbers, '5', 1),
    '55': find_repeating_digits(block_numbers, '5', 2),
    '555': find_repeating_digits(block_numbers, '5', 3),
    '5555': find_repeating_digits(block_numbers, '5', 4),
    '55555': find_repeating_digits(block_numbers, '5', 5),    '6': find_repeating_digits(block_numbers, '6', 1),
    '66': find_repeating_digits(block_numbers, '6', 2),
    '666': find_repeating_digits(block_numbers, '6', 3),
    '6666': find_repeating_digits(block_numbers, '6', 4),
    '66666': find_repeating_digits(block_numbers, '6', 5),
    '7': find_repeating_digits(block_numbers, '7', 1),
    '77': find_repeating_digits(block_numbers, '7', 2),
    '777': find_repeating_digits(block_numbers, '7', 3),
    '7777': find_repeating_digits(block_numbers, '7', 4),
    '77777': find_repeating_digits(block_numbers, '7', 5),
    '8': find_repeating_digits(block_numbers, '8', 1),
    '88': find_repeating_digits(block_numbers, '8', 2),
    '888': find_repeating_digits(block_numbers, '8', 3),
    '8888': find_repeating_digits(block_numbers, '8', 4),
    '88888': find_repeating_digits(block_numbers, '8', 5),
    '9': find_repeating_digits(block_numbers, '9', 1),
    '99': find_repeating_digits(block_numbers, '9', 2),
    '999': find_repeating_digits(block_numbers, '9', 3),
    '9999': find_repeating_digits(block_numbers, '9', 4),
    '99999': find_repeating_digits(block_numbers, '9', 5),
    'Palindrome 5': find_palindromes(block_numbers, 5),
    'Palindrome 6': find_palindromes(block_numbers, 6),
    'Multiples of 7': find_multiples(block_numbers, 7),
    'Multiples of 11': find_multiples(block_numbers, 11),
    'Multiples of 12': find_multiples(block_numbers, 12),
    'Multiples of 13': find_multiples(block_numbers, 13),
    'Multiples of 14': find_multiples(block_numbers, 14),
    'Multiples of 15': find_multiples(block_numbers, 15),
    'Multiples of 16': find_multiples(block_numbers, 16),
    'Multiples of 17': find_multiples(block_numbers, 17),
    'Multiples of 18': find_multiples(block_numbers, 18),
    'Multiples of 19': find_multiples(block_numbers, 19),
    'Multiples of 33': find_multiples(block_numbers, 33),
    'Multiples of 69': find_multiples(block_numbers, 69),
    'Contains 108': find_contains(block_numbers,108),
    'Contains 321': find_contains(block_numbers,321),
    'Contains 420': find_contains(block_numbers,420),
    'Contains 1089': find_contains(block_numbers,1089),
    'Contains 4761': find_contains(block_numbers,4761),
    'Contains 28980': find_contains(block_numbers,28980),
    'Contains 176400': find_contains(block_numbers,176400),
    '3-digit Powers of 7': powers_of_7_counts[3],
    '4-digit Powers of 7': powers_of_7_counts[4],
    '5-digit Powers of 7': powers_of_7_counts[5],
    '6-digit Powers of 7': powers_of_7_counts[6],
    '3-digit Fibonacci': find_fibonacci(block_numbers, 3),
    '4-digit Fibonacci': find_fibonacci(block_numbers, 4),
    '5-digit Fibonacci': find_fibonacci(block_numbers, 5),
    '6-digit Fibonacci': find_fibonacci(block_numbers, 6)
}

# Find all embedded perfect squares
embedded_perfect_squares = {3: [], 4: [], 5: [], 6: []}

for block in block_numbers:
    for digit_length in embedded_perfect_squares.keys():
        embedded_squares = find_embedded_perfect_squares(block, digit_length)
        if embedded_squares:
            embedded_perfect_squares[digit_length].append((block, embedded_squares))

def count_digits_in_positions(numbers):
    max_length = max(len(num) for num in numbers)
    digit_counts = {f"D{i}": {str(d): 0 for d in range(10)} for i in range(max_length)}

    for num in numbers:
        reversed_num = num[::-1]  # Reverse the number to start counting from the end
        for i, digit in enumerate(reversed_num):
            digit_counts[f"D{i}"][digit] += 1

    return digit_counts

# Create DataFrames for each digit length
dfs_squares = {digit_length: pd.DataFrame(data, columns=['Block Number', f'Embedded {digit_length}-Digit Perfect Squares'])
               for digit_length, data in embedded_perfect_squares.items()}

# Create a summary DataFrame for perfect squares
summary_data_squares = {f'{digit_length}-Digit Perfect Squares': len(data) for digit_length, data in embedded_perfect_squares.items()}
summary_df_squares = pd.DataFrame(list(summary_data_squares.items()), columns=['Digit Length', 'Count'])

# Calculate gematria for each block
gematria_results_1digit = [(block, calculate_gematria(block, single_digit=True)) for block in block_numbers]
gematria_results_2digit = [(block, calculate_gematria(block, single_digit=False)) for block in block_numbers]

# Create DataFrames for the gematria results
gematria_df_1digit = pd.DataFrame(gematria_results_1digit, columns=['Block', 'Gematria 1-Digit'])
gematria_df_2digit = pd.DataFrame(gematria_results_2digit, columns=['Block', 'Gematria 2-Digit'])

# Create summaries of the gematria results
gematria_summary_1digit = gematria_df_1digit['Gematria 1-Digit'].value_counts().sort_index()
gematria_summary_df_1digit = pd.DataFrame(gematria_summary_1digit).reset_index()
gematria_summary_df_1digit.columns = ['Gematria 1-Digit', 'Count']

gematria_summary_2digit = gematria_df_2digit['Gematria 2-Digit'].value_counts().sort_index()
gematria_summary_df_2digit = pd.DataFrame(gematria_summary_2digit).reset_index()
gematria_summary_df_2digit.columns = ['Gematria 2-Digit', 'Count']

# Count the digits in each position
digit_counts = count_digits_in_positions(block_numbers)

# Convert the results to a DataFrame for easier viewing
df_digits = pd.DataFrame(digit_counts).transpose()

# Convert the results to a DataFrame
# Convert the results to a DataFrame
summary_patterns = {
    key: value[1] if isinstance(value, tuple) else value
    for key, value in patterns.items()
}
summary_df_patterns = pd.DataFrame(list(summary_patterns.items()), columns=['Pattern', 'Count'])

# Create summaries of the gematria results
gematria_summary_1digit = gematria_df_1digit['Gematria 1-Digit'].value_counts().sort_index()
gematria_summary_df_1digit = pd.DataFrame(gematria_summary_1digit).reset_index()
gematria_summary_df_1digit.columns = ['Pattern', 'Count']
gematria_summary_df_1digit['Pattern'] = 'Gematria 1-Digit: ' + gematria_summary_df_1digit['Pattern'].astype(str)

gematria_summary_2digit = gematria_df_2digit['Gematria 2-Digit'].value_counts().sort_index()
gematria_summary_df_2digit = pd.DataFrame(gematria_summary_2digit).reset_index()
gematria_summary_df_2digit.columns = ['Pattern', 'Count']
gematria_summary_df_2digit['Pattern'] = 'Gematria 2-Digit: ' + gematria_summary_df_2digit['Pattern'].astype(str)

# Consolidate all summaries into a single DataFrame
summary_df = pd.concat([
    summary_df_patterns,
    summary_df_squares.rename(columns={'Digit Length': 'Pattern'}),
    gematria_summary_df_1digit,
    gematria_summary_df_2digit,
    df_digits.sum(axis=1).reset_index().rename(columns={'index': 'Pattern', 0: 'Count'})
])

# Save the results to an Excel file with separate tabs
output_file = 'block_analysis_patterns.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl', mode='w') as writer:
    summary_df.to_excel(writer, sheet_name='Summary', index=False)
    
    for pattern, value in patterns.items():
        if isinstance(value, tuple):
            blocks, count = value
            df = pd.DataFrame(blocks, columns=[pattern])
            df.to_excel(writer, sheet_name=pattern, index=False)
      
    for digit_length, blocks in powers_of_7.items():
        if blocks:
            df = pd.DataFrame(blocks, columns=[f'Power of 7 - {digit_length} Digits'])
            df.to_excel(writer, sheet_name=f'Power of 7 - {digit_length} Digits', index=False)
     
    for digit_length, df in dfs_squares.items():
        df.to_excel(writer, sheet_name=f'{digit_length}-Digit Squares', index=False)
    
    gematria_df_1digit.to_excel(writer, sheet_name='Gematria 1-Digit Results', index=False)
    gematria_df_2digit.to_excel(writer, sheet_name='Gematria 2-Digit Results', index=False)
    
    for column in df_digits.columns:
        df_digits[[column]].to_excel(writer, sheet_name=f'Digit Counts - {column}', index=True)
    # Create a summary DataFrame for digit counts
    digit_counts_summary = []
    for position, counts in digit_counts.items():
        for digit, count in counts.items():
            digit_counts_summary.append([f"{position} = {digit}", count])

    digit_counts_summary_df = pd.DataFrame(digit_counts_summary, columns=['Position and Digit', 'Count'])

    digit_counts_summary_df.to_excel(writer, sheet_name='Digit Counts Summary', index=False)


print(f"Results saved to {output_file}")

# Log the input data
print(f"Length of block_numbers: {len(block_numbers)}")
print(f"Sample block numbers: {block_numbers[:10]}")

# Log the patterns and their counts
print("Patterns and their counts:")
for pattern, value in patterns.items():
    if isinstance(value, (list, tuple)):
        blocks, count = value
        print(f"{pattern}: {count}")
    else:
        print(f"{pattern}: {value}")

# Log the summary patterns and their counts
print("Summary patterns and their counts:")
for pattern, count in summary_patterns.items():
    print(f"{pattern}: {count}")

# Log the final summary DataFrame
print("Final summary DataFrame:")
print(summary_df)






