import streamlit as st
import pandas as pd

# Google Sheet ka public link yahan paste karein
SHEET_URL = "APNI_GOOGLE_SHEET_CSV_LINK_YAHAN_PASTE_KAREIN"

st.title("💍 Shahzeb Premium Jewelry")
st.write("Hamari latest jewelry collection dekhein aur WhatsApp par rabta karein.")

try:
    # Data load karna
    df = pd.read_csv(SHEET_URL)

    for index, row in df.iterrows():
        with st.container(border=True):
            st.subheader(row['Product Name'])
            # Agar sheet mein Image_URL hai to image dikhayein
            if 'Image_URL' in row and pd.notna(row['Image_URL']):
                st.image(row['Image_URL'], width=200)
            
            st.write(f"**Price:** {row['Price']}")
            st.write(f"**Details:** {row['Details']}")
            
            # Aapka WhatsApp link yahan set hai
            whatsapp_link = f"https://wa.me/923016372254?text=Mujhe {row['Product Name']} pasand aaya hai."
            st.link_button("Order via WhatsApp", whatsapp_link)

except Exception as e:
    st.error("Google Sheet ka link check karein ya data load nahi ho raha.")
    
