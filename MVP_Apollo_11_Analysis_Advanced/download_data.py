
import os
import requests
from config import DATA_URLS, DOWNLOAD_DIR

def download_files():
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    
    for url in DATA_URLS:
        filename = os.path.join(DOWNLOAD_DIR, url.split("/")[-1])
        response = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {filename}")

if __name__ == "__main__":
    download_files()
