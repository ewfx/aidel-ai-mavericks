import spacy

nlp = spacy.load("en_core_web_trf")

def process_unstructured_transaction(transaction_text: str) -> dict:
    
    result = {
        "sender": {
            "org": [],
            "person": [],
            "locations": set()
        },
        "receiver": {
            "org": [],
            "person": [],
            "locations": set()
        },
        "additionalNotes": {
            "org": [],
            "person": [],
            "locations": set()
        }
    }

    sections = {
    "sender": (transaction_text.find("Sender:"), transaction_text.find("Receiver:")),
    "receiver": (transaction_text.find("Receiver:"), transaction_text.find("Additional Notes:")),
    "additionalNotes": (transaction_text.find("Additional Notes:"), len(transaction_text))
}

    doc = nlp(transaction_text)
    for ent in doc.ents:
        entity_text = ent.text.strip('"')
        entity_label = ent.label_
        for section, (start, end) in sections.items():
            if ent.start_char >= start and ent.end_char <= end:
                
                if entity_label == "ORG":
                    result[section]["org"].append(entity_text)
                elif entity_label == "PERSON":
                    result[section]["person"].append(entity_text)
                elif entity_label == "GPE":
                    result[section]["locations"].add(entity_text)
    for section in result:
        result[section]["locations"] = list(result[section]["locations"])
    return result;