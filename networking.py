import sqlite3
from datetime import datetime

conn = sqlite3.connect("networking.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        firm TEXT,
        role TEXT,
        email TEXT,
        how_met TEXT,
        date_met TEXT,
        last_contacted TEXT,
        notes TEXT
    )
""")

conn.commit()
conn.close()

date_met = datetime.now().strftime("%Y-%m-%d")

def add_contact():
    name = input("Name: ")
    firm = input("Firm: ")
    role = input("Role: ")
    email = input("Email: ")
    how_met = input("How did you meet? ")
    today = datetime.now().strftime("%Y-%m-%d")
    date_met = today
    last_contacted = today
    notes = input("Notes: ")
    conn = sqlite3.connect("networking.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO contacts (name, firm, role, email, how_met, date_met, last_contacted, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, firm, role, email, how_met, date_met, last_contacted, notes))
    
    conn.commit()
    conn.close()

def view_contacts():
    conn = sqlite3.connect("networking.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    
    for row in rows:
        print(f"Name: {row[1]} | Firm: {row[2]} | Role: {row[3]} | Last contacted: {row[7]}")

    
    conn.close()

def log_interaction():
    name = input("Name of contact: ")
    conn = sqlite3.connect("networking.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
    row = cursor.fetchone()
    
    if row is None:
        print("Contact not found.")
        return
    
    new_note = input("Note about this interaction: ")
    today = datetime.now().strftime("%Y-%m-%d")
    updated_notes = row[8] + f" | {today}: {new_note}"

    cursor.execute("UPDATE contacts SET last_contacted = ?, notes = ? WHERE name = ?", 
               (today, updated_notes, name))
    
    conn.commit()
    print(f"Interaction logged for {name}.")
    conn.close()

def view_reminders():
    conn = sqlite3.connect("networking.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, last_contacted FROM contacts")
    rows = cursor.fetchall()
    
    print("Contacts to reach out to:")
    for row in rows:
        last_contacted = datetime.strptime(row[1], "%Y-%m-%d")
        days_since_contact = (datetime.now() - last_contacted).days
        if days_since_contact > 30:
            print(f"{row[0]} (last contacted {days_since_contact} days ago)")

    conn.close()

def print_menu():
    print("=============================")
    print("  NETWORKING TRACKER v1.0")
    print("=============================")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Log interaction")
    print("4. View reminders")
    print("5. Exit")

while True:
    print_menu()
    choice = input("Select option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        log_interaction()
    elif choice == "4":
        view_reminders()
    elif choice == "5":
        print("Good Luck out there. ")
        break
    else:
        print("Invalid option. Please try again.")