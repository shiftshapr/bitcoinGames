import pandas as pd
import math

# Function to check if a number is a perfect square
def is_perfect_square(n):
    root = math.isqrt(n)
    return n == root * root

# Function to find all 4 or 5-digit perfect squares within a block number
def find_embedded_perfect_squares(block):
    embedded_squares = []
    block_str = str(block)
    length = len(block_str)
    
    for i in range(length - 3):
        for j in range(4, 6):  # Check 4 and 5 digit substrings
            if i + j <= length:
                num_str = block_str[i:i + j]
                num = int(num_str)
                if is_perfect_square(num):
                    embedded_squares.append(num)
    
    return embedded_squares

import sys

# Check if the input file is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 analysis2Gematria.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Read the block numbers from the file
with open(input_file, 'r') as f:
    blocks = [int(line.strip()) for line in f]

# Find all embedded perfect squares
embedded_perfect_squares = []

for block in blocks:
    embedded_squares = find_embedded_perfect_squares(block)
    if embedded_squares:
        embedded_perfect_squares.append((block, embedded_squares))

# Create a DataFrame to display the results
df = pd.DataFrame(embedded_perfect_squares, columns=['Block Number', 'Embedded Perfect Squares'])

# Save the results to an Excel file
output_file = 'embedded_perfect_squares.xlsx'
df.to_excel(output_file, index=False)

print(f"Results saved to {output_file}")
