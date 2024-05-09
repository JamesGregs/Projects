import csv
import os
import logging
import time
from datetime import datetime, timedelta
from flask import Flask, jsonify
import schedule
import threading

# Initialize Flask
app = Flask(__name__)

# Configuration for logging system
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define constants for directory
PROJECT_FOLDER = 'onebyzero'
WEB_APP = 'web_app'
TRANSACTION_INFO = 'transaction_info'
TRANSACTION_REF = 'transaction_ref'

# Load CSV into a list of dictionaries
def load_csv_data(file_path):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            return list(csv.DictReader(file))
    except Exception as e:
        logging.error(f"Failed to read {file_path}: {e}")
        return []

# Load transaction data and reference data then merge based on key -> productId
def load_and_merge_data(transactions_path, reference_path, key):
    transactions = []
    for filename in os.listdir(transactions_path):
        if filename.endswith('.csv'):
            data = load_csv_data(os.path.join(transactions_path, filename))
            transactions.extend(data)

    ref_data = {item[key]: item for filename in os.listdir(reference_path)
                for item in load_csv_data(os.path.join(reference_path, filename))
                if filename.endswith('.csv')}

    return [{**trans, **ref_data.get(trans[key], {})} for trans in transactions]

# List holding all transaction data
transactions = []

# Update data and checks transaction info for new .csv file or update on those files
def update_transactions():
    transactions_path = os.path.join(os.getcwd(), PROJECT_FOLDER, WEB_APP, TRANSACTION_INFO)
    reference_path = os.path.join(os.getcwd(), PROJECT_FOLDER, WEB_APP, TRANSACTION_REF)
    global transactions
    transactions = load_and_merge_data(transactions_path, reference_path, 'productId')
    logging.info("Transaction data updated")

# Run continuosly based on defined schedule
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Update transaction every 30 seconds
schedule.every(30).seconds.do(update_transactions)
# Start a daemon thread to run the schededuler function
threading.Thread(target=run_scheduler, daemon=True).start()

# Filter transaction by date
def filter_transactions_by_date(last_n_days, key):
    cutoff_date = datetime.now() - timedelta(days=last_n_days)
    return [trans for trans in transactions if datetime.strptime(trans[key], '%Y-%m-%d %H:%M:%S') >= cutoff_date]

# Summarize transaction depend on attribute
def summarize_transactions(filtered_transactions, group_by):
    summary = {}
    for trans in filtered_transactions:
        identifier = trans[group_by]
        amount = float(trans['transactionAmount'])
        summary[identifier] = summary.get(identifier, 0) + amount
    
    if group_by == 'productName':
        summary_list = [{'productName': key, "totalAmount": value} for key, value in summary.items()]
    elif group_by == 'productManufacturingCity':
        summary_list = [{"cityName": key, "totalAmount": value} for key, value in summary.items()]

    return summary_list

# Route to get info on single transaction based on ID
@app.route('/assignment/transaction/<transaction_id>')
def get_transaction(transaction_id):
    transaction = next((trans for trans in transactions if trans['transactionId'] == transaction_id), None)
    if transaction:
        formatted_transaction = {
            'transactionId': transaction['transactionId'],
            'productName': transaction['productName'],
            'transactionAmount': float(transaction['transactionAmount']),
            'transactionDatetime': transaction['transactionDatetime']
        }
        return jsonify(formatted_transaction)
    return jsonify({"error": "Transaction not found"}), 404

# Route to get summary of transactions by product over the last specified date
@app.route('/assignment/transactionSummaryByProducts/<int:last_n_days>')
def transaction_summary_by_products(last_n_days):
    filtered_transactions = filter_transactions_by_date(last_n_days, 'transactionDatetime')
    formatted_summary = summarize_transactions(filtered_transactions, 'productName')
    return jsonify({"summary": formatted_summary})

# Route to get summary of transactions by city over the last specified date
@app.route('/assignment/transactionSummaryByManufacturingCity/<int:last_n_days>')
def transaction_summary_by_manufacturing_city(last_n_days):
    filtered_transactions = filter_transactions_by_date(last_n_days, 'transactionDatetime')
    formatted_summary = summarize_transactions(filtered_transactions, 'productManufacturingCity')
    return jsonify({"summary": formatted_summary})

if __name__ == '__main__':
    app.run(debug=True)
