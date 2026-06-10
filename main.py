from fastapi import FastAPI
from dotenv import load_dotenv
import requests
import socket
import time
import os
import uvicorn
from bs4 import BeautifulSoup
import google.generativeai as genai

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


# -----------Layer 2: Content Extractor----------
def extract_text(html:str):
    soup = BeautifulSoup(html, "html.parser")
    
    # Remove script and style elements
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()
    
    # get clean text
    text = soup.get_text(separator=" ")

    # remove extra white space
    clean = " ".join(text.split())

    # limit to 1500 characters
    return clean[:1500]


#-----------Layer 3: AI Summary------------
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def get_ai_summary(text:str):
    prompt=f"""
    Based on this website content, write a clear 2-3 sentence 
    summary of what this website is about. Be specific and direct.

    Content:{text}
    """
    response = model.generate_content(prompt)
    return response.text


# test endpoint
@app.get("/")
def home():
    return {"message": "Website Intelligence Tool is running!"}

@app.get("/inspect")
def inspect(url:str):
    #Layer1: networking
    network_info, raw_html = get_network_info(url)

    #layer2: extract clean text
    clean_text=extract_text(raw_html)

    #layer3: AI summary
    Summary=get_ai_summary(clean_text)

    #combine everything into one response
    return {
        **network_info,
        "clean_text": clean_text,
        "ai_summary": Summary
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

