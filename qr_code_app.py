import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", page_icon="🔳")

st.title("🔳 Simple QR Code Generator")

st.markdown("### 1️⃣ Paste your URL or text below")
data = st.text_input("URL or text")

st.markdown("### 2️⃣ Define the name of the QR code image (without .png)")
filename = st.text_input("Image file name", value="my_qr_code")

if st.button("Generate QR Code"):
    if data and filename:
        img = qrcode.make(data)
        buf = BytesIO()
        img.save(buf, format="PNG")
        st.image(buf.getvalue(), caption="Your QR Code", use_column_width=False)
        st.download_button(
            label="Download QR Code",
            data=buf.getvalue(),
            file_name=f"{filename}.png",
            mime="image/png"
        )
    else:
        st.warning("❗ Please fill in both fields above.")