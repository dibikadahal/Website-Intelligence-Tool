# 🌐 Website Intelligence Tool
A full-stack web application that analyzes any URL and returns 
complete technical networking data combined with an AI-powered 
content summary — built with Python, FastAPI, and Streamlit.

---

## 🎯 What It Does

Paste any URL and instantly get:

- 🔍 **DNS Lookup** — Resolves the domain to its real IP address
- 📡 **HTTP Inspection** — Status code, response time, server type
- 🔒 **HTTPS Check** — Verifies if SSL/TLS is active
- 🤖 **AI Summary** — Gemini AI summarizes what the website is about

---

## 📸 Screenshots

### Main Interface
<img width="1250" height="602" alt="image" src="https://github.com/user-attachments/assets/8c6c6bb3-fac3-47d1-a3cb-e184624b7044" />


### Analysis Results
<img width="1005" height="636" alt="image" src="https://github.com/user-attachments/assets/01dfe6d3-6d99-4488-b5e4-423ac92d3bea" />

### AI Summary
<img width="774" height="238" alt="image" src="https://github.com/user-attachments/assets/6a0b52e1-b72e-4859-88d0-14ff764c5241" />

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Backend API | FastAPI + Python | HTTP endpoints, routing |
| Networking | socket, requests | DNS lookup, HTTP inspection |
| HTML Parsing | BeautifulSoup4 | Extract clean text from pages |
| AI Summary | Google Gemini API | Intelligent content summarization |
| Frontend | Streamlit | Interactive web interface |
| Server | Uvicorn | ASGI server for FastAPI |

---

## 🧠 Networking Concepts Applied

This project directly demonstrates the following concepts in real code:

- **DNS Resolution** — `socket.gethostbyname()` converts domain 
  names to IP addresses
- **HTTP Protocol** — Real GET requests with status codes, 
  response headers, and timing
- **HTTPS/TLS Detection** — Checks for SSL certificate presence
- **TCP Connections** — Every request runs over TCP underneath
- **REST API Design** — FastAPI endpoint with proper HTTP methods 
  and status codes
- **Ports** — Backend runs on port 8000, frontend on port 8501

---

## 📁 Project Structure

    website-intelligence/
    │
    ├── main.py            # FastAPI backend — all networking logic
    ├── frontend.py        # Streamlit UI — user interface
    ├── requirements.txt   # All dependencies
    ├── .env               # API keys (not in repo)
    ├── .gitignore         # Ignores .env and venv
    └── assets/            # Screenshots for README
---

## 🚀 Run Locally

### Prerequisites
- Python 3.9+
- Google Gemini API key (free at aistudio.google.com)

### Setup

```bash
# Clone the repository
git clone https://github.com/dibikadahal/Website-Intelligence-Tool.git
cd Website-Intelligence-Tool

# Create virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo GEMINI_API_KEY=your_key_here > .env
```

### Run

Open two terminals:

**Terminal 1 — Backend:**
```bash
py main.py
```

**Terminal 2 — Frontend:**
```bash
streamlit run frontend.py
```

Open `http://localhost:8501` in your browser.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| GET | `/inspect?url=<url>` | Full website analysis |
| GET | `/docs` | Interactive API documentation |

### Example Response

```json
{
  "domain": "github.com",
  "ip_address": "140.82.121.4",
  "status_code": 200,
  "response_time_ms": 183,
  "server": "GitHub.com",
  "https": true,
  "content_type": "text/html; charset=utf-8",
  "ai_summary": "GitHub is a platform where developers 
                 host, share, and collaborate on code."
}
```

---

## 💡 What I Learned

Building this project gave me hands-on experience with:

- How DNS resolution works in real code
- Making and reading HTTP requests and responses
- Understanding status codes, headers, and response timing
- Integrating a third-party AI API
- Building and consuming a REST API
- Structuring a full-stack Python project

---

## 👩‍💻 Author

**Dibika Dahal**  
[GitHub](https://github.com/dibikadahal) · 
[LinkedIn](https://www.linkedin.com/in/dibika-dahal-a720642b0/)
