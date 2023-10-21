*** List of Tools ***

1. Value Extraction Tool: Extracts principal funds from PDFs and saves the data to a new CSV file, considering any issues related to the month and year stated in the document.

2. Table Import Tool: Imports all downloaded loan-level data to a database, making it accessible for querying purposes.

3. Data Validation Tool: Compares the number of rows in the imported database table with the number of rows in the loan-level data to ensure data accuracy and completeness.

4. Total Principal Calculator Tool: Generates a new CSV file that contains calculated total principal data in alignment with the statement date from the certificate holders statement.

5. Merging Tool: Merges the CSV files created by the value extraction tool and the calculator tool based on the statement date. Additionally, it generates a new column that compares the total principal with the principal funds available.

--------------------------------------------------------------------------

*** Usage ***

This scripts doesn't have prompt(for future) to run. It can be launch through CLI or Terminals using python command. 

--------------------------------------------------------------------------

If you encounter any bugs, issues, or have any suggestions for improvement please contact the author.

*** Author ***

James Martin Gregorio
jmgregorio48@gmail.com

--------------------------------------------------------------------------

*** Version ***

1. value_extraction_tool_ver1 - Initial release
2. table_import_tool_ver3 - Initial release
3. data_validation_tool_ver0 - Initial release
4. total_principal_calculator_ver0 - Initial release
5. merging_and_compare_tool_ver0 - Initial release

