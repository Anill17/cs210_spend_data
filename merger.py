import pandas as pd
import os

# Define the directory containing the cleaned CSV files
cleaned_dir = 'csvs/cleaned'
output_file = 'csvs/cleaned/merged_cleaned_data.csv'

# List of cleaned CSV files to merge
csv_files = [
    os.path.join(cleaned_dir, 'ccozet1_cleaned.csv'),
    os.path.join(cleaned_dir, 'ccozet2_cleaned.csv'),
    os.path.join(cleaned_dir, 'ccozet3_cleaned.csv')
]

# Initialize an empty list to hold DataFrames
dataframes = []

# Read each CSV file and process it
for file in csv_files:
    try:
        print(f"Processing file: {file}")  # Log the file being processed
        df = pd.read_csv(file)
        
        # Remove everything from the start to and including "KAZANILAN MİL" in the "Açıklama" column
        df['AÇIKLAMA'] = df['AÇIKLAMA'].apply(lambda x: x.split('KAZANILAN MİL', 1)[-1].strip() if 'KAZANILAN MİL' in x else x)
        
        # Append the DataFrame to the list
        dataframes.append(df)
    except pd.errors.ParserError as e:
        print(f"Error reading {file}: {e}")  # Log the error
    except Exception as e:
        print(f"An unexpected error occurred with {file}: {e}")

# Concatenate all DataFrames into a single DataFrame if any were successfully read
if dataframes:
    merged_df = pd.concat(dataframes, ignore_index=True)
    # Write the merged DataFrame to a new CSV file
    merged_df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Merged data has been saved to {output_file}.")
else:
    print("No valid dataframes to merge.")