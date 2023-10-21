import os
import csv
import psycopg2

# Function to infer data types from the CSV file
def infer_data_types(csv_file_path):
    with open(csv_file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        sample_data = next(reader)

    data_types = []
    for value in sample_data:
        if value.isdigit():
            data_types.append('INTEGER')
        elif is_float(value):
            data_types.append('NUMERIC')
        else:
            data_types.append('VARCHAR(255)')

    return header, data_types

# Function to check if a string can be converted to a float
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Function to get row count from a CSV file
def get_csv_row_count(csv_file_path):
    with open(csv_file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        return sum(1 for row in reader)

### Future plan to use prompt instead of hard coding the database/user details ###
# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname='CMLTI06AMC1',
    user='postgres',
    password='@jmGreg_04postgres',
    host='localhost',
    port='5432'
)
cur = conn.cursor()

# Schema name where your tables are stored
schema_name = 'last_super_final_test'

# Folder path containing the CSV files
folder_path = 'C:/Users/Gregs/ML Projects/Loan-level_Data/'  # Replace with your folder path

# List to store table names
table_names = []

# Retrieve all the CSV file paths in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Function to compare the data between a table and a CSV file
def validate_data(table_name, csv_file_path):
    # Check row count in CSV file
    csv_row_count = get_csv_row_count(csv_file_path)

    # Check row count in the corresponding table
    cur.execute(f"SELECT COUNT(*) FROM {schema_name}.{table_name};")
    table_row_count = cur.fetchone()[0]

    # Compare row counts
    if csv_row_count != table_row_count:
        print(f"Data mismatch for {table_name}. Row count in CSV: {csv_row_count}, Row count in table: {table_row_count}")

# Iterate through each CSV file in the folder
for csv_file in csv_files:
    # CSV file path
    csv_file_path = os.path.join(folder_path, csv_file)

    # Table name from the CSV file name
    table_name = os.path.splitext(csv_file)[0]  # Get the file name without the extension
    table_names.append(table_name)

    # Perform data validation for the current table and CSV file
    validate_data(table_name, csv_file_path)

# Close the connection
cur.close()
conn.close()
