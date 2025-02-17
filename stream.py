import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyAlCtdrEW48j2rPrVaBtmEEebaxDf-qf8M")
st.title("🚀 AI Python Code Reviewer")
st.write("Submit your Python code for AI-powered review and improvements.")

# Input for Python code
user_prompt = st.text_area("Give your code here:", height=250)

# Button to review code
if st.button("Generate Code"):
    model = genai.GenerativeModel(model_name='models/gemini-2.0-flash',
    system_instruction="""You are a friendly AI assistant.
    Given a Python code to review, analyze the submitted code and identify bugs, errors, and areas of improvement.
    Provide the fixed code snippets.
    Explain the reasoning behind code correlations or suggestions.
    If the code is not in Python, politely remind the user that you are a Python code review assistant.""")
    
    if user_prompt:
        response = model.generate_content(user_prompt)
        st.write(response.text)
