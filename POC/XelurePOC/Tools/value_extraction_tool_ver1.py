import time
import os
import PyPDF2
import csv
import re

# Record the start time
start_time = time.time()

# Directory containing the PDF files
directory = 'Datasets/'

# Define the target string
target_string = "Total Principal Funds Available"

# Output CSV file to save the extracted data
output_file = 'extracted_TPFA.csv'

# Open the CSV file in write mode with a CSV writer
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Date', 'Total Principal Funds Available'])
     
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                num_pages = len(reader.pages)

                # Initialize the extracted value to None
                value = None

                # Search for the target string in each page
                for page_num in range(num_pages):
                    page = reader.pages[page_num]
                    text = page.extract_text()
                    
                    # print(f"Extracted text from {filename}: {text}")
                    # Check if the target string exists in the page
                    if target_string in text:
                        # Extract the value for "Total Principal Funds Available"
                        start_index = text.find(target_string)
                        end_index = text.find('\n', start_index)
                        raw_value = text[start_index + len(target_string):end_index].strip()
                        
                        value = re.sub(r'[^0-9,\.]', '', raw_value).replace(',', '')

                # Write the extracted value and filename to the CSV file
                writer.writerow([filename[-6:-4] + "/" +filename[-8:-6], value])

# Print a message when the process is complete
print("Data extraction and CSV creation completed.")

# Record the end time
end_time = time.time()

runtime = end_time - start_time
print(f"Runtime: {runtime:.4f} seconds")