import streamlit as st

from openai import OpenAI
f = open(r"C:\Users\shiny\Downloads\open_ai\.open_api_key.txt")
key = f.read()

client = OpenAI(api_key=key)
st.title(":red[An AI Code Reviewer]")

# Text area for user input
prompt = st.text_area("Enter your Python code here", height=200)

# Button to trigger code review
button = st.button("Generate")

if button:
    st.subheader("Code Review")

    # Generate code review using OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant. Given Python code, suggest improvements."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract and display the fixed code
    fixed_code = response.choices[0].message.content
    st.title("Fixed Code")
    st.code(fixed_code, language='python')
