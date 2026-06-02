import streamlit as st
import pandas as pd

# Sheet ki URL yahan paste karein
SHEET_ID = "YOUR_GOOGLE_SHEET_ID_HERE"
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

# Data load karein
def load_data():
    return pd.read_csv(URL)

st.title("Jewelry Store: Live from Google Sheets")

# Data display
data = load_data()

col1, col2, col3 = st.columns(3)
for index, row in data.iterrows():
    with [col1, col2, col3][index % 3]:
        st.subheader(row['Product Name'])
        st.write(f"Price: {row['Price']}")
        st.markdown(f"[Buy Now]({row['Affiliate_Link']})")
      
