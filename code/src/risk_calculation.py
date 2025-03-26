import os
import re
from groq import Groq
from fastapi import FastAPI, HTTPException
import json

client = Groq(
    api_key = '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',
)

risk_assessment_prompt = """
You are a financial risk assessment AI specializing in transaction analysis.  
Your task is to analyze the given transaction details and provide a structured JSON output with the following fields:  

1. **Risk Score** (0-1) → Overall transaction risk.  
2. **Confidence Score** (0-1) → Confidence in the assessment based on source reliability.  
3. **Supporting Evidence** → A list of sources (e.g., financial reports, regulatory filings, news articles, crime databases, PEP lists, POI lists etc) **that directly contribute to the risk score** (e.g., sanctions, fraud history, legal violations). **Do not include generic background information. Only include source name**  
4. **Reason** → A concise explanation of why this risk score was given, **citing only the sources that influenced the risk assessment** (e.g., frauds, sanctions, financial instability, crimes).  
5. **Extracted Entity** → A list of entities extracted from the transaction
6. **Entity Type** → A list of entity types (e.g., person, corporation, shell company, NGO, etc.) for the extracted entities. **If any source identifies a company as a Shell Company, classify it as Shell Company in the Entity Type **
7. **Transaction ID** → Transaction ID given in the transaction

**IMPORTANT:**  
- Do not output any other fields or information except these seven fields.  
- No other text should be present. Do not include ```. Only return a valid JSON.  
- **Only include sources that contain evidence affecting the risk score.** Do not include sources that only provide general background information.  
- Do not explain the methodology; only state the risk factors considered and their impact on the score.  

### **Risk Calculation Formula**  
Risk Score = (Sender Risk * 0.5) + (Receiver Risk * 0.3) + (Intermediary Risk * 0.2)

Special Case: If no intermediary is involved, redistribute its weight equally:
Risk Score = (Sender Risk * 0.5) + (Receiver Risk * 0.5) 

- **Sender Risk (50%)**: Fraud history, financial instability, legal/regulatory issues of the sender.  
- **Receiver Risk (30% or 50%)**: Financial weakness, fraud allegations, sanctions, or instability of the receiver.  
- **Intermediary Risk (20%)** *(If applicable)* → Risks related to any facilitating entities.
- **Consider VPN usage and transaction locations when assessing risk. Locations which are sanctioned should be considered risky**

The **Confidence Score** depends on the availability, credibility, and consistency of the sources used.

**Input Format (Transaction Details)**  
Transaction: [Full description of the transaction, including sender, receiver, intermediaries, amount, and context]

**Additional Information for Analysis**  
**Use only authoritative financial reports, regulatory filings, and credible sources (e.g., OpenCorporates, SEC Edgar, OpenSanctions, WikiData, OFAC, World Bank PEP List, crime databases).
If evidence is lacking, note uncertainty while making a best-effort assessment. Also, consider the involvement of subsidiaries in frauds/crimes**  
"""

def analyze_risk(transaction: str):
    try:
        final_prompt = risk_assessment_prompt +"\n"+ transaction

        print("starting response generation\n")
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": final_prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=500,
            timeout=30,
        )
        output_text = response.choices[0].message.content.strip()
       
        json_match = re.search(r'\{.*\}', output_text, re.DOTALL)
        if not json_match:
            print(f"Failed to extract JSON. Raw response: {output_text}")
            return {"error": "Invalid JSON format returned by model", "raw_response": output_text}

        json_text = json_match.group()

        try:
            output_json = json.loads(json_text)  # Safe JSON parsing
            
        except json.JSONDecodeError as e:
            print(f"JSON Parsing Error: {e}, Raw Response: {json_text}")
            return {"error": "Invalid JSON format returned by model", "raw_response": json_text}

        return output_json
    
    except Exception as e:
        return {"error": str(e)}