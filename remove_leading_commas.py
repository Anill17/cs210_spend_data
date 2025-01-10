import os

# List of CSV files to process
csv_files = ['csvs/ccozet1.csv', 'csvs/ccozet2.csv', 'csvs/ccozet3.csv']

for file_path in csv_files:
    # Read the original file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Remove leading commas from each line
    cleaned_lines = [line.lstrip(',') for line in lines]

    # Write the cleaned lines back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(cleaned_lines)

print("Leading commas removed from the specified CSV files.")