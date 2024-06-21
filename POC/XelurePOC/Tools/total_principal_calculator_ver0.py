import csv
import psycopg2

### Future plan to use prompt instead of hard coding the database/user details ###
# Establish a connection to the database
connection = psycopg2.connect(user="postgres",
                              password="@jmGreg_04postgres",
                              host="localhost",
                              port="5432",
                              database="CMLTI06AMC1")

# Create a cursor
cursor = connection.cursor()

# Define the schema and query to be executed
schema = 'last_super_final_test'
query = """
SELECT 
    SUM(scheduled_principal) + SUM(curtailments) + SUM(curtailment_adjustments) + SUM(other_principal_adjustments) + SUM(prepayment) + SUM(repurchase_principal) + SUM(liquidation_principal) + SUM(principal_recoveries) - SUM(principal_losses) AS total_amount
FROM 
    {schema}.{table_name};
"""

# Get all table names from the schema
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = '{}'".format(schema))
table_names = cursor.fetchall()

# Iterate over table names and execute the query for each table
results = {}
for table in table_names:
    cursor.execute(query.format(schema=schema, table_name=table[0]))
    result = cursor.fetchone()[0]
    results[table[0]] = result

# Close the cursor and connection
cursor.close()
connection.close()

# Write results to a CSV file
csv_file_path = "extracted_total_payment.csv"
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Total Amount"])
    for table, amount in results.items():
        writer.writerow([table[-2:] + "/" + table[-4:-2], amount])

# Print a success message
print("Results have been exported to", csv_file_path)
