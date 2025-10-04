import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from slang_dict import slang_dict

# Download punkt tokenizer for Streamlit Cloud
nltk.download('punkt')

# App config
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

# Function: Slang → Formal
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
        st.warning("⚠️ দয়া করে কিছু টেক্সট লিখুন।")

# Extra Features (Optional)
st.markdown("---")
st.info(
    "📌 Future Features: \n"
    "- Banglish Detection\n"
    "- Large Slang Database\n"
    "- Download Formal Text\n"
    "- ML-based Smart Conversion"
)
