import pdfplumber
import os
from groq import Groq

path = input("Enter the path to the PDF file: ")

with pdfplumber.open(path) as pdf:
    text = "\n".join(page.extract_text() for page in pdf.pages)

job_description = input("Paste the job description: ")

prompt = f"""
You are a career advisor. Analyse the following resume against the job description.

Resume:
{text}

Job Description:
{job_description}

Return exactly:
1. Match score (percentage)
2. Strong matches (skills present in both)
3. Missing skills (in JD but not in resume)
4. One specific recommendation

Be concise and direct.
"""

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}]
)

print("=============================")
print("  CV ANALYSER")
print("=============================")
print(response.choices[0].message.content)
print("=============================")