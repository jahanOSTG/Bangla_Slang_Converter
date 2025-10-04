import os
import nltk
from nltk.tokenize import word_tokenize
import streamlit as st
from slang_dict import slang_dict  # তোমার slang_dict.py থেকে

# ========================
# NLTK punkt tokenizer setup
# ========================
# Streamlit Cloud বা local machine উভয়ের জন্য
nltk_data_path = os.path.join(os.path.dirname(__file__), "nltk_data")
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)

nltk.data.path.append(nltk_data_path)

# punkt tokenizer download only if not already present
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", download_dir=nltk_data_path)

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
    tokens = word_tokenize(text)
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
