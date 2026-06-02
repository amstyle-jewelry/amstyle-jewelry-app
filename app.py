import streamlit as st

st.set_page_config(page_title="Shahzeb Jewelry Catalog", layout="centered")

st.title("💍 Shahzeb Premium Jewelry")
st.write("Hamari latest jewelry collection dekhein aur WhatsApp par rabta karein.")

# Inventory (Yahan aap apne products edit kar sakte hain)
products = [
    {"name": "Gold Ring 22K", "price": "PKR 50,000", "desc": "Pure gold with hallmark"},
    {"name": "Silver Necklace", "price": "PKR 15,000", "desc": "Handcrafted silver"},
    {"name": "Bridal Set", "price": "PKR 120,000", "desc": "Heavy gold work"}
]

for p in products:
    with st.container(border=True):
        st.subheader(p['name'])
        st.write(f"**Price:** {p['price']}")
        st.write(f"**Details:** {p['desc']}")
        # Direct WhatsApp Link
        st.link_button("Order via WhatsApp", "https://wa.me/923XXXXXXXXXX") 
