
# config.py
DATA_URLS = [
    "https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19710015566.pdf",
    "https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19700008096.pdf",
    "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11_MissionOpReport.pdf"
]

DOWNLOAD_DIR = "apollo_data"
CLEANED_DATA_FILE = "apollo_data/cleaned_data.csv"
MAX_TOKENS = 5000
SEQUENCE_LENGTH = 100
BATCH_SIZE = 32
EPOCHS = 10
