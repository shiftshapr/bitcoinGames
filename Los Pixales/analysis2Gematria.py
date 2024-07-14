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

# Function to calculate 2-digit gematria number
def calculate_gematria(block):
    sum_digits = sum(int(digit) for digit in block)
    while sum_digits >= 100:
        sum_digits = sum(int(digit) for digit in str(sum_digits))
    return sum_digits

# Calculate gematria for each block
gematria_results = [(block, calculate_gematria(block)) for block in blocks]

# Create a DataFrame for the gematria results
gematria_df = pd.DataFrame(gematria_results, columns=['Block', 'Gematria'])

# Create a summary of the gematria results
gematria_summary = gematria_df['Gematria'].value_counts().sort_index()
gematria_summary_df = pd.DataFrame(gematria_summary).reset_index()
gematria_summary_df.columns = ['Gematria', 'Count']

# Save the results to an Excel file
with pd.ExcelWriter('block_gematria_analysis.xlsx') as writer:
    gematria_df.to_excel(writer, sheet_name='Gematria Results', index=False)
    gematria_summary_df.to_excel(writer, sheet_name='Summary', index=False)

print(gematria_summary_df)
