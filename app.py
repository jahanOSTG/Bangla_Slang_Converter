# app.py

import streamlit as st
from slang_dict import slang_dict  

# ========================
<<<<<<< HEAD
# NLTK punkt tokenizer setup
# ========================
nltk_data_path = os.path.join(os.path.dirname(__file__), "nltk_data")
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)

nltk.data.path.append(nltk_data_path)

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", download_dir=nltk_data_path)

# ========================
=======
>>>>>>> fb7ef63dd4a9d8bb025e6c29547c274c0212d869
# Streamlit App Config
# ========================
st.set_page_config(
    page_title="Slang → Formal Converter",
    page_icon="📝",
    layout="centered"
)

# ========================
# Custom CSS for Styling
# ========================
st.markdown("""
    <style>
        body {
            font-family: "Segoe UI", sans-serif;
        }
        .main-title {
            font-size: 2.2rem;
            color: #1f77b4;
            font-weight: bold;
            text-align: center;
        }
        .sub-title {
            font-size: 1.1rem;
            color: #444444;
            text-align: center;
            margin-bottom: 20px;
        }
        .stTextArea textarea {
            border-radius: 12px;
            border: 2px solid #1f77b4;
            font-size: 16px;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            font-weight: 600;
            border-radius: 10px;
            padding: 8px 20px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #16679a;
            transform: scale(1.05);
        }
        .result-box {
            background: #f8f9fa;
            border-left: 5px solid #1f77b4;
            padding: 12px;
            border-radius: 10px;
            font-size: 17px;
            color: #222222;
        }
    </style>
""", unsafe_allow_html=True)

# ========================
# Header Section
# ========================
col1, col2, col3 = st.columns([1,2,1])  # মধ্যের column বড়, দুই পাশে ছোট
with col2:
    st.image("assets/logo.jpeg", width=150)


st.markdown('<div class="main-title">📝 Slang → Formal Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title" style="color: #FFD700;">Casual Bangla Slang কে Formal Bangla টেক্সটে রূপান্তর করুন 🚀</div>', unsafe_allow_html=True)


# ========================
# Input Section
# ========================
user_input = st.text_area("👉 আপনার Slang টেক্সট লিখুন:", "", height=120)

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

# ========================
# Button & Output
# ========================
if st.button("🚀 Convert Now"):
    if user_input.strip() != "":
        output = slang_to_formal(user_input)
        st.markdown("### ✅ Formal Text:")
        st.markdown(f'<div class="result-box">{output}</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ দয়া করে কিছু টেক্সট লিখুন।")

# ========================
# Footer Section
# ========================
st.markdown("---")
st.caption("⚡ Developed with ❤️ using Streamlit | Future Features: Banglish Detection • ML-based Conversion • Download Option")
