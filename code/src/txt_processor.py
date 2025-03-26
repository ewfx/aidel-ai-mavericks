from typing import List, Dict, Any
import re

def process_txt_file(content_str: str) -> List[Dict[str, Any]]:
    all_results = []
    transactions = content_str.split("---")
    for transaction_text in transactions:
        transaction_text = transaction_text.strip()
        
        lines = transaction_text.split("\n")
        cleaned_text = "" 
        for line in lines:
            line=re.sub(r'[“”\'"]', '', line).strip()
            cleaned_text += line + "\n" 
        cleaned_text = cleaned_text.strip()

        all_results.append(cleaned_text)
    return all_results