import csv
import os

# Create a cleaned directory if it doesn't exist
output_dir = 'csvs/cleaned'
os.makedirs(output_dir, exist_ok=True)

# List of input and output CSV files
csv_files = {
    'csvs/ccozet1.csv': os.path.join(output_dir, 'ccozet1_cleaned.csv'),
    'csvs/ccozet2.csv': os.path.join(output_dir, 'ccozet2_cleaned.csv'),
    'csvs/ccozet3.csv': os.path.join(output_dir, 'ccozet3_cleaned.csv')
}

def clean_line(line):
    # Clean the line by handling quotes and commas
    # Replace commas within quotes with a placeholder
    line = line.replace('"', '""')  # Escape quotes
    line = ','.join(filter(None, line.split(',')))  # Remove extra commas
    return line.strip(',')            # Remove leading/trailing commas

for input_file, output_file in csv_files.items():
    cleaned_lines = []
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            for row in reader:
                # Clean each row
                cleaned_row = [clean_line(str(cell)) for cell in row]
                cleaned_lines.append(cleaned_row)

        # Write the cleaned lines to a new CSV file
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(cleaned_lines)

    except Exception as e:
        print(f"Error processing {input_file}: {e}")

print("Data has been cleaned and saved to the cleaned directory.")