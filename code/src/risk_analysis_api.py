
from fastapi import FastAPI, File, UploadFile, HTTPException
from risk_analysis_processor import process_file_content

app = FastAPI()

@app.post("/process_transactions")
async def process_transactions(file: UploadFile = File(...)):
    if file.filename.endswith(".csv"):
        file_type = "csv"
    elif file.filename.endswith(".txt"):
        file_type = "txt"
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type. Please upload a .csv or .txt file.")
    
    content = await file.read()
    content_str = content.decode("utf-8")
    content_str = content_str.replace("\r\n", "\n").replace("\r", "\n")
    content_str = content_str.replace("\u2028", "\n").replace("\u2029", "\n")
    return process_file_content(content_str, file_type)
    
    