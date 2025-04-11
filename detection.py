from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables (make sure GOOGLE_API_KEY is set in your .env file)
load_dotenv()

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Streamlit App
st.set_page_config(page_title="Language Detector with Gemini", layout="centered")
st.title("🌐 Language Detection App")
st.write("Enter a sentence and I'll guess the language!")

# Input from user
user_input = st.text_area("Enter your text:", height=150)

if st.button("Detect Language"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        prompt = f"""You are a language detection model. 
Identify the language of the following text and provide the name of the language only (no explanation):

Text: {user_input}"""

        try:
            response = llm.invoke(prompt)
            language = response.content.strip()
            st.success(f"Detected Language: **{language}**")
        except Exception as e:
            st.error(f"Error: {e}")
