
import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

st.set_page_config(page_title="AI Photo Studio VIP", page_icon="📸", layout="centered")

# Custom Styling for Professional Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; background-color: #ff4b4b; color: white; font-weight: bold; border-radius: 8px; }
    .premium-tag { color: #ffd700; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("👑 AI Photo Studio VIP")
st.subheader("Duniya Ka Behtareen AI Photo Enhancer & Filter Studio")
st.write("---")

uploaded_file = st.file_uploader("📸 Apni Photo Upload Karein Ya Drop Karein:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Original Photo", use_container_width=True)
    
    st.write("---")
    st.markdown("### 🌟 Instant Pro Filters (Kholte Hi Active)")
    
    # 12 Professional & Premium Filters
    filter_type = st.radio("Koi Ek Professional Filter Select Karein:", [
        "✨ Auto-Beautify Pro",
        "✨ HDR Rich Color",
        "✨ Soft Portrait Blur",
        "⚫ Classic Black & White",
        "🎨 Pencil Sketch Art",
        "🔒 Gold Glow VIP (Premium)",
        "🔒 Cyberpunk Neon (Premium)",
        "🔒 Vintage 1990s (Premium)",
        "🔒 Cinematic Mood (Premium)",
        "🔒 Ultra Sharp 4K (Premium)"
    ])
    
    processed_image = image.copy()
    is_premium = "🔒" in filter_type
    
    # Filter Logic
    if filter_type == "✨ Auto-Beautify Pro":
        processed_image = ImageEnhance.Sharpness(processed_image).enhance(2.0)
        processed_image = ImageEnhance.Color(processed_image).enhance(1.2)
    elif filter_type == "✨ HDR Rich Color":
        processed_image = ImageEnhance.Contrast(processed_image).enhance(1.5)
        processed_image = ImageEnhance.Color(processed_image).enhance(1.6)
    elif filter_type == "✨ Soft Portrait Blur":
        processed_image = image.filter(ImageFilter.GaussianBlur(radius=3))
    elif filter_type == "⚫ Classic Black & White":
        processed_image = ImageOps.grayscale(processed_image)
    elif filter_type == "🎨 Pencil Sketch Art":
        processed_image = image.filter(ImageFilter.CONTOUR)
    elif filter_type == "🔒 Gold Glow VIP (Premium)":
        processed_image = ImageEnhance.Color(processed_image).enhance(2.0)
    elif filter_type == "🔒 Cyberpunk Neon (Premium)":
        processed_image = ImageOps.colorize(ImageOps.grayscale(processed_image), "#00ffcc", "#ff00ff")
    elif filter_type == "🔒 Vintage 1990s (Premium)":
        processed_image = ImageEnhance.Contrast(processed_image).enhance(0.8)
    elif filter_type == "🔒 Cinematic Mood (Premium)":
        processed_image = ImageEnhance.Brightness(processed_image).enhance(0.9)
        processed_image = ImageEnhance.Contrast(processed_image).enhance(1.3)
    elif filter_type == "🔒 Ultra Sharp 4K (Premium)":
        processed_image = image.filter(ImageFilter.SHARPEN)

    with col2:
        st.image(processed_image, caption="Filtered Result", use_container_width=True)

    st.write("---")
    st.markdown("### 🎛 Pro Manual Tools")
    exposure = st.slider("Brightness (Exposure)", 0.5, 2.0, 1.0)
    contrast = st.slider("Contrast Level", 0.5, 2.0, 1.0)
    
    if exposure != 1.0:
        processed_image = ImageEnhance.Brightness(processed_image).enhance(exposure)
    if contrast != 1.0:
        processed_image = ImageEnhance.Contrast(processed_image).enhance(contrast)

    st.write("---")
    
    if is_premium:
        st.warning("⚠️ Yeh Premium Filter hai. Isay download karne ke liye user ko Subscription leni hogi.")
        if st.button("💳 Unlock All Premium Filters ($1.99/Month)"):
            st.success("💰 Payment Gateway Connected! (Real App mein yahan se JazzCash/Card se paise katenge)")
    else:
        st.success("✅ Free Filter! Aap isay download kar sakte hain.")
        st.button("📥 Download Filtered Photo")
    
