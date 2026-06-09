import requests
import hashlib
import json
import os
from datetime import datetime

pages = {
    "Macquarie": "https://www.macquarie.com/au/en/careers/early-careers.html",
    "JPMorgan": "https://careers.jpmorgan.com/au/en/students/programs",
    "Morgan Stanley": "https://www.morganstanley.com/people/students-graduates",
    "Goldman Sachs": "https://www.goldmansachs.com/careers/students/",
    "CBA": "https://www.commbank.com.au/about-us/careers/graduates.html",
    "NAB": "https://www.nab.com.au/about-us/careers/early-careers",
    "Westpac": "https://www.westpac.com.au/about-westpac/working-with-us/early-careers/",
    "Deloitte": "https://www2.deloitte.com/au/en/careers/students-graduates.html",
    "KPMG": "https://www.kpmg.com.au/careers/students-graduates/",
    "PwC": "https://www.pwc.com.au/careers/student-and-graduate.html",
    "EY": "https://www.ey.com/en_au/careers/students",
    "Grant Thornton": "https://www.grantthornton.com.au/careers/students-and-graduates/",
}

current = {}

if os.path.exists("snapshot.json"):
    with open("snapshot.json", "r") as f:
        previous = json.load(f)
else:
    previous = {}

print("=============================")
print("  CAREER PAGE MONITOR")
print("=============================")
print(f"Checked: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print()

for name, url in pages.items():
    try:
        response = requests.get(url, timeout=10)
        current[name] = hashlib.md5(response.text.encode()).hexdigest()
        if previous.get(name) == current[name]:
            print(f"✓ {name} — no change")
        else:
            print(f"⚠ {name} — CHANGED (check for new roles)")
    except:
        print(f"{name}: failed to fetch")
        current[name] = None

hash = {
    "Macquarie": "8f2486794cd61375c05705e24fd37893",
    "Deloitte": "46ed22c58dc2bfc51b26ac08cca1a5e5"
}

with open("snapshot.json", "w") as f:
    json.dump(current, f)
