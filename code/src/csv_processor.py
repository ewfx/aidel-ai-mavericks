import csv
from io import StringIO
from typing import List, Dict, Any

def process_csv_file(content_str: str) -> List[Dict[str, Any]]:
    csv_reader = csv.DictReader(StringIO(content_str))
    all_results = []
    for row in csv_reader:
        result = {
                    "sender": {
                        "org": [],
                        "person": [],
                        "locations": []
                    },
                    "receiver": {
                        "org": [],
                        "person": [],
                        "locations": []
                    },
                    "additionalNotes": {
                        "org": [],
                        "person": [],
                        "locations": []
                    }
                }
        sender=row.get("Payer Name", ""),
        receiver=row.get("Receiver Name", ""),
        receiver_country=row.get("Receiver Country", "")
        transaction_id=row.get("Transaction ID", "")
        result["sender"]["org"] = sender
        result["receiver"]["org"] = receiver
        result["receiver"]["locations"]= receiver_country
        result["transactionId"] = transaction_id;
        all_results.append(result)

    return all_results