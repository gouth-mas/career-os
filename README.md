# Career OS

An AI-powered career operating system built in Python. Five interconnected 
modules covering every stage of the internship and graduate recruitment process.

Built by a UNSW Commerce student (Accounting + AI in Business & Society) 
targeting corporate finance and corporate law roles.

---

## Modules

### Stage 1 — Application Tracker
Terminal-based tracker for logging internship and graduate applications. 
Stores company, role, status, deadline, and notes. Persists data to CSV 
with full CRUD functionality.

**Stack:** Python, pandas, CSV

---

### Stage 2 — CV Analyser
Upload a resume PDF and paste a job description. Returns a match score, 
strong matches, missing skills, and a targeted recommendation — powered 
by an LLM via the Groq API.

**Stack:** Python, pdfplumber, Groq API (Llama 3.3)

---

### Stage 3 — Career Page Monitor
Monitors career pages for target firms using MD5 hashing. Detects any 
content changes since the last run and flags them — no more manually 
checking 12 firm websites.

**Target firms:** Macquarie, JPMorgan, Deloitte, KPMG, PwC

**Stack:** Python, requests, hashlib, JSON

---

### Stage 4 — Networking CRM
SQLite-powered contact manager for tracking everyone met at careers events, 
coffee chats, and info sessions. Logs interactions, updates relationship 
warmth, and surfaces contacts not reached out to in 30+ days.

**Stack:** Python, SQLite3

---

### Stage 5 — Streamlit Dashboard
Web dashboard pulling all four modules into a single interface. Three pages: 
Applications, Networking, and Monitor — all live data, no refresh needed.

**Stack:** Python, Streamlit, pandas, SQLite3

---

## How to run

```bash
pip install pandas pdfplumber requests streamlit groq watchdog
python tracker.py        # Application tracker
python cv_analyser.py    # CV analyser  
python monitor.py        # Career page monitor
python networking.py     # Networking CRM
streamlit run dashboard.py  # Launch dashboard
```

## Libraries
pandas, pdfplumber, requests, streamlit, groq, sqlite3, hashlib, json
