import streamlit as st
from utility.generate_response import generate_content, create_prompt
from utility.speech import generate_audio, speech_to_text, play_audio  
import pyttsx3
import asyncio

# Streamlit app layout
st.title("SheikhGPT")

# Initialize pyttsx3 engine for text-to-speech
engine = pyttsx3.init()

# User input
if 'response' not in st.session_state:
    st.session_state['response'] = ''

user_query = st.chat_input("Enter your Islamic query:")


if user_query:
    prompt = create_prompt(user_query)
    response = generate_content(prompt)  # Generate the response based on the user query
    st.write("Response:")
    st.write(response)
    filepath = asyncio.run(generate_audio(response))
    if st.button("Speak Response"):
        # audio_file = generate_audio(response)  # Generate audio
        play_audio(filepath) 
            
            
else:
        st.warning("Please enter a query.")


# Add button for speech-to-text
if st.button("Speak Input"):
    with st.spinner("Listening..."):
        user_query = speech_to_text()  # Capture speech input
    st.text_input("Enter your Islamic query:", value=user_query)  # Update input field with recognized text
