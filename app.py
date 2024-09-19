import streamlit as st
from utility.generate_response import generate_content, create_prompt  # Import your AI model function


# Streamlit app layout
st.title("Islamic Content Generation App")

# User input
user_query = st.text_input("Enter your Islamic query:")

if st.button("Get Response"):
    if user_query:
        prompt = create_prompt(user_query)
        response = generate_content(prompt)  # Control the user query
        st.write("Response:")
        st.write(response)
    else:
        st.warning("Please enter a query.")