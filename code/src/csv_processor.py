import csv
from io import StringIO
from typing import List, Dict, Any

def process_csv_file(content_str: str) -> List[Dict[str, Any]]:
    csv_reader = csv.DictReader(StringIO(content_str))
    all_results = []
    for row in csv_reader:
        text = ""
        text=text + "Transaction ID: "+row.get("Transaction ID", "") + "\n"
        text=text + "Payer Name: "+row.get("Payer Name", "") + "\n"
        text=text + "Receiver Name: "+row.get("Receiver Name", "") + "\n"
        text=text + "Transaction Details: "+row.get("Transaction Details", "") + "\n"
        text=text + "Amount: "+row.get("Amount", "") + "\n"
        text=text + "Receiver Country: "+row.get("Receiver Country", "")
        all_results.append(text)

    return all_results