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

# Strip newlines and convert to strings
block_numbers = [num.strip() for num in block_numbers]

# Function to count digits in each position from the end
def count_digits_in_positions(numbers):
    max_length = max(len(num) for num in numbers)
    digit_counts = {f"D{i}": {str(d): 0 for d in range(10)} for i in range(max_length)}

    for num in numbers:
        reversed_num = num[::-1]  # Reverse the number to start counting from the end
        for i, digit in enumerate(reversed_num):
            digit_counts[f"D{i}"][digit] += 1

    return digit_counts

# Count the digits in each position
digit_counts = count_digits_in_positions(block_numbers)

# Convert the results to a DataFrame for easier viewing
df = pd.DataFrame(digit_counts).transpose()

# Save the results to an Excel file
df.to_excel('block_digit_counts.xlsx', index=True)

# Print results for verification
print(df)
