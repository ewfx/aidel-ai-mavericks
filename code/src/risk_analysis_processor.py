
from typing import List, Dict, Any
import txt_processor, csv_processor
from risk_calculation import analyze_risk
def process_file_content(content_str: str, file_type : str) -> List[Dict[str, Any]]:
    if file_type == "csv":
        result = csv_processor.process_csv_file(content_str)
    else:  
        result = txt_processor.process_txt_file(content_str)

    for transaction in result:
        analyze_risk(transaction)
    return ""