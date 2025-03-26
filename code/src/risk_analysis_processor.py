
from typing import List, Dict, Any
import txt_processor, csv_processor
from risk_calculation import analyze_risk
def process_file_content(content_str: str, file_type : str) -> List[Dict[str, Any]]:
    if file_type == "csv":
        result = csv_processor.process_csv_file(content_str)
    else:  
        result = txt_processor.process_txt_file(content_str)
    all_results=[]
    for transaction in result:
        all_results.append(analyze_risk(transaction))
    return all_results