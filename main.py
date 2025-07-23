from fastapi import FastAPI, Request
from log_fetcher import fetch_logs

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "SAP CPI Log API is running"}

@app.get("/logs")
def get_logs():
    logs = fetch_logs()
    return logs
