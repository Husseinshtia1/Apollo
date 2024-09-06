from pdfminer.high_level import extract_text
import os
import pandas as pd
from config import DOWNLOAD_DIR, CLEANED_DATA_FILE

def extract_text_from_pdf(pdf_path):
    try:
        return extract_text(pdf_path)
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return ""

def clean_and_save_data():
    texts = []
    for file in os.listdir(DOWNLOAD_DIR):
        if file.endswith(".pdf"):
            pdf_text = extract_text_from_pdf(os.path.join(DOWNLOAD_DIR, file))
            if pdf_text:  # Only add non-empty text
                texts.append(pdf_text)
    
    df = pd.DataFrame({"text": texts})
    df.to_csv(CLEANED_DATA_FILE, index=False)
    print(f"Data cleaned and saved to {CLEANED_DATA_FILE}")

if __name__ == "__main__":
    clean_and_save_data()
