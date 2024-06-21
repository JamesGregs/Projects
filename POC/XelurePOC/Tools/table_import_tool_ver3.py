import os
import psycopg2
import csv

# Function to infer data types from the CSV file
def infer_data_types(csv_file_path):
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        sample_data = next(reader)

    data_types = []
    for value in sample_data:
        if is_integer(value):
            data_types.append('INTEGER')
        elif is_float(value):
            data_types.append('NUMERIC')
        else:
            data_types.append('VARCHAR(255)')

    return header, data_types

# Function to check if a string can be converted to an integer
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Function to check if a string can be converted to a float
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

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

# Schema name to be created
schema_name = 'last_super_final_test'

# SQL command to create a new schema
create_schema_query = f"CREATE SCHEMA {schema_name};"

# Execute the CREATE SCHEMA statement
cur.execute(create_schema_query)

# Folder path containing the CSV files
folder_path = 'C:/Users/Gregs/ML Projects/Loan-level_Data'

# Retrieve all the CSV file paths in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Function to insert data into the table
def insert_data_into_table(csv_file_path, schema_name, table_name, cur, conn):
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            # Preprocess the row before insertion
            processed_row = preprocess_data(row)
            placeholders = ', '.join(['%s'] * len(processed_row))
            insert_query = f"INSERT INTO {schema_name}.{table_name} VALUES ({placeholders})"
            cur.execute(insert_query, processed_row)
        conn.commit()

# Function for data preprocessing
def preprocess_data(row):
    for i in range(len(row)):
        # Convert appropriate numerical values to integers or floats
        if row[i] != '' and is_float(row[i]):
            if '.' in row[i]:
                row[i] = float(row[i])  # Convert to float if the value contains a decimal point
            else:
                row[i] = int(row[i])  # Convert to integer if the value is a whole number
        elif row[i] == '':  # Convert empty strings to NULL
            row[i] = None
    return row

        
        
for i, csv_file in enumerate(csv_files):
    
    # CSV file path
    csv_file_path = os.path.join(folder_path, csv_file)
    
    # Infer data types from the CSV file
    header, data_types = infer_data_types(csv_file_path)
    
    # Generate the CREATE TABLE statement
    table_name = os.path.splitext(csv_file)[0]  
    # Generate the CREATE TABLE statement
    create_table_query = f"CREATE TABLE {schema_name}.{table_name} ("

    for col, data_type in zip(header, data_types):
        # Replace spaces and '&' characters with underscores
        col_cleaned = col.replace(' ', '_').replace('&', '_and_').replace('/', '_or_').replace(',', '_or').replace('#', 'Num').replace('+', '_plus_').replace('%', '_percent_')
        create_table_query += f"{col_cleaned} {data_type}, "
    create_table_query = create_table_query.rstrip(', ') + ");"

    # Execute the CREATE TABLE statement
    cur.execute(create_table_query)
    conn.commit()
    
    # Insert data into the table
    insert_data_into_table(csv_file_path, schema_name, table_name, cur, conn)

# Close the connection
cur.close()
conn.close()
