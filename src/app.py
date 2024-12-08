import os
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    # Create sample transaction data as a list of dictionaries
    transactions = [
        {'id': i, 'success': 1 if i % 5 != 0 else 0} 
        for i in range(1, 101)
    ]
    
    # Calculate success rate without pandas
    total_transactions = len(transactions)
    successful = sum(t['success'] for t in transactions)
    success_rate = (successful / total_transactions) * 100
    
    return (
        f"Sales Transaction Success Rate: {success_rate:.1f}%<br>"
        f"Successful Transactions: {successful}<br>"
        f"Total Transactions: {total_transactions}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)