import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
SAS_TOKEN = os.getenv("SAS_TOKEN")

def fetch_logs():
    full_url = f"{BASE_URL}{SAS_TOKEN}"
    headers = {"Accept": "application/json"}

    response = requests.get(full_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get('d', {}).get('results', [])
    else:
        return {"error": response.status_code, "message": response.text}
