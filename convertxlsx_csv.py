import pandas as pd
import os

def excel_to_csv(excel_file, csv_file):
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file)
        
        # Convert to CSV
        df.to_csv(csv_file, index=False)
        print(f"Successfully converted {excel_file} to {csv_file}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def convert_all_excel_files(input_directory, output_directory):
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Get all xlsx files in the input directory
    excel_files = [f for f in os.listdir(input_directory) if f.endswith('.xlsx')]
    
    for excel_file in excel_files:
        input_path = os.path.join(input_directory, excel_file)
        output_path = os.path.join(output_directory, excel_file.replace('.xlsx', '.csv'))
        excel_to_csv(input_path, output_path)

# Example usage - updated with csvs output directory
if __name__ == "__main__":
    try:
        # Specify input and output directories
        input_directory = "cc-history-xlsx"
        output_directory = "csvs"  # Changed to output to /csvs/ directory
        
        print(f"Looking for Excel files in: {input_directory}")
        
        # List all xlsx files in the specified directory
        print("\nExcel files found:")
        for file in os.listdir(input_directory):
            if file.endswith('.xlsx'):
                print(f"- {file}")
        
        print("\nConverting all Excel files...")
        print(f"CSV files will be saved to: {output_directory}/")
        convert_all_excel_files(input_directory, output_directory)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
