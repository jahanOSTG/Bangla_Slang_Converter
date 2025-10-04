# app.py

import streamlit as st
from slang_dict import slang_dict  # তোমার slang_dict.py থেকে

# ========================
# Streamlit App Config
# ========================
st.set_page_config(
    page_title="Bangla Slang → Formal Converter",
    page_icon="📝",
    layout="centered"
)

# Header
st.image("assets/logo.jpeg", width=100)
st.title("📝 Bangla Slang → Formal Converter")
st.subheader("Casual Bangla Slang কে Formal Bangla টেক্সটে রূপান্তর করুন।")

# Input Box
user_input = st.text_area("👉 আপনার Slang টেক্সট লিখুন:", "")

# ========================
# Function: Slang → Formal
# ========================
def slang_to_formal(text):
    """
    Simple Bangla-friendly tokenizer using space-based split.
    This avoids NLTK/Tokenizer issues and works on Streamlit Cloud.
    """
    if not text.strip():
        return ""
    tokens = text.split()  # Space-based tokenizer
    converted_tokens = [slang_dict.get(token.lower(), token) for token in tokens]
    return " ".join(converted_tokens)

# Button & Output
if st.button("Convert"):
    if user_input.strip() != "":
        output = slang_to_formal(user_input)
        st.success("✅ Formal Text:")
        st.write(output)
    else:
        st.warning("⚠️ দয়া করে কিছু টেক্সট লিখুন।")

# Extra Features (Optional)
st.markdown("---")
st.info(
    "📌 Future Features:\n"
    "- Banglish Detection\n"
    "- Large Slang Database\n"
    "- Download Formal Text\n"
    "- ML-based Smart Conversion"
)
