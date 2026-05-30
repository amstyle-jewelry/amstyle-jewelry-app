import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter

st.set_page_config(page_title="AI Photo Studio Pro", page_icon="📸", layout="centered")

st.title("📸 AI Photo Studio Pro")
st.subheader("Professional AI Photo Editor & Enhancer")
st.write("---")

uploaded_file = st.file_uploader("Apni Tasvir Upload Karein (JPG/PNG):", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_container_width=True)
    st.write("---")
    
    st.markdown("### 🛠 AI Editing & Enhancement Tools")
    
    # 1. Auto Enhance & Filters
    tool_option = st.selectbox("Koi AI Tool Select Karein:", [
        "Select a Tool", 
        "Auto Enhance (Beautify)", 
        "AI Background Blur", 
        "Black & White Filter", 
        "Sketch Effect"
    ])
    
    processed_image = image.copy()
    
    if tool_option == "Auto Enhance (Beautify)":
        enhancer = ImageEnhance.Sharpness(processed_image)
        processed_image = enhancer.enhance(2.0)
        enhancer = ImageEnhance.Color(processed_image)
        processed_image = enhancer.enhance(1.3)
        st.success("✨ Auto Enhance Applied!")
        
    elif tool_option == "AI Background Blur":
        processed_image = image.filter(ImageFilter.GaussianBlur(radius=4))
        st.success("🎯 Background Blurred Successfully!")
        
    elif tool_option == "Black & White Filter":
        processed_image = image.convert("L")
        st.success("⚫ Black & White Filter Applied!")
        
    elif tool_option == "Sketch Effect":
        processed_image = image.filter(ImageFilter.CONTOUR)
        st.success("✏️ Sketch Effect Applied!")

    # 2. Manual Adjustments
    if tool_option != "Select a Tool":
        st.write("---")
        st.markdown("### 🎛 Manual Adjustments")
        
        exposure = st.slider("Brightness (Exposure)", 0.5, 2.0, 1.0)
        contrast = st.slider("Contrast", 0.5, 2.0, 1.0)
        
        if exposure != 1.0:
            enhancer = ImageEnhance.Brightness(processed_image)
            processed_image = enhancer.enhance(exposure)
        if contrast != 1.0:
            enhancer = ImageEnhance.Contrast(processed_image)
            processed_image = enhancer.enhance(contrast)
            
        st.image(processed_image, caption="Processed Image", use_container_width=True)
        st.write("🎉 Aapki professional app tayyar hai! Mazeed features jald update honge.")
      
