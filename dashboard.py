import streamlit as st
import pandas as pd
import sqlite3
import json

page = st.sidebar.selectbox("Navigate", ["Applications", "Networking", "Monitor"])

if page == "Applications":
    st.title("Applications Dashboard")
    df = pd.read_csv("applications.csv")
    st.dataframe(df)

elif page == "Networking":
    st.title("Networking Dashboard")
    conn = sqlite3.connect('networking.db')
    df = pd.read_sql_query("SELECT * FROM contacts", conn)
    st.dataframe(df)
    conn.close()

elif page == "Monitor":
    st.title("Monitor Dashboard")
    with open("snapshot.json", "r") as f:
        data = json.load(f)
    
    monitor_df = pd.DataFrame([
        {"Firm": firm, "Last Hash": hash[:8] + "..."}
        for firm, hash in data.items()
    ])
    st.dataframe(monitor_df)