from fastapi import FastAPI
from dotenv import load_dotenv
import requests
import socket
import time
import os
import uvicorn
from bs4 import BeautifulSoup

# load the .env file
load_dotenv()

app = FastAPI()

# -----------Layer 1: Networking Inspector-----------
def get_network_info(url : str):
    result = {}

    # Step1: Get the domain and IP address
    domain = url.replace("https://", "").replace("http://", "").split("/")[0]
    result['domain'] = domain
    result['ip_address'] = socket.gethostbyname(domain)

    # Step2: HTTP Request (State, speed, server)
    start = time.time()
    response = requests.get(url, timeout = 10)
    end = time.time()

    result["status_code"] = response.status_code
    result["response_time_ms"] = round((end - start) * 1000)
    result["server"] = response.headers.get("Server", "Not disclosed")
    result["https"] = url.startswith("https://")
    result["content_type"] = response.headers.get("Content-Type", "Unknown")

    return result, response.text

# test endpoint
@app.get("/")
def home():
    return {"message": "Website Intelligence Tool is running!"}

@app.get("/inspect")
def inspect(url:str):
    network_info, _ = get_network_info(url)
    return {"network_info": network_info}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

