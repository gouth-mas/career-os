import pandas as pd
import os

# load or create the applications CSV
if os.path.exists("applications.csv"):
    df = pd.read_csv("applications.csv")
else: 
    df = pd.DataFrame(columns=["company", "role", "date_applied", "status",  "link", "notes"])

def print_menu():
    print("=============================")
    print("  CAREER TRACKER v1.0")
    print("=============================")
    print("1. Add application")
    print("2. View Applications")
    print("3. View Updated Application Status")
    print("4. Filter Applications")
    print("5. Exit")

def add_application(df):
    company = input("Company name: ")
    role = input("Role: ")
    date_applied = input("Date of Application: ")
    status = input("Status: ")
    link = input("Link: ")
    notes = input("Notes: ")
    new_row = {"company": company, "role": role, "date_applied": date_applied, "status": status, "link": link, "notes": notes}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv("applications.csv", index=False)
    return df

def view_applications(df):
    print(df.to_string(index=False))

def update_status(df):
    company = input("Company Name: ")
    match = df[df["company"] == company]
    if len(match) == 0:
        print("Company not found.")
        return df
    print(f"Current Status: {match['status'].values[0]}")
    new_status = input("Updated Status: ")
    df.loc[df["company"] == company, "status"] = new_status
    return df

def filter_applications(df):
    status = input("Filter by status: ")
    filtered = df[df["status"] == status]
    if len(filtered) == 0:
        print("Status Filter Unsuccessful")
    else:
        print(filtered.to_string(index=False))

while True:
    print_menu()
    choice = input("Select option: ")

    if choice == "1":
        df = add_application(df)
    elif choice == "2":
        view_applications(df)
    elif choice == "3":
        df = update_status(df)       # returns updated df
    elif choice == "4":
        filter_applications(df)
    elif choice == "5":
        print("Good luck out there. ")
        break
    else:
        print("Invalid option. Try again. ")

