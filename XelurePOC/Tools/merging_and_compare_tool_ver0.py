import csv
import pandas as pd

# Load the resulting table data
csv_file_path1 = "extracted_total_payment.csv"
data1 = pd.read_csv(csv_file_path1)

# Load the other CSV file
csv_file_path2 = "extracted_TPFA.csv"
data2 = pd.read_csv(csv_file_path2)

# Sort both dataframes based on the common column
data1 = data1.sort_values(by="Date")
data2 = data2.sort_values(by="Date")

# Merge the two dataframes based on a common column
merged_data = pd.merge(data1, data2, on="Date", how="inner")

# Add a new column to indicate if two columns are equal
merged_data['Comparison'] = merged_data.apply(lambda row: 'Match' if row['Total Amount'] == row['Total Principal Funds Available'] else 'Not Match', axis=1)


# Save the merged data to a new CSV file
merged_csv_file_path = "total_principal_v_TPFA.csv"
merged_data.to_csv(merged_csv_file_path, index=False)

# Print a success message
print("Merged data has been exported to", merged_csv_file_path)
