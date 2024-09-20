import streamlit as st
import edge_tts  # For text-to-speech

from utility.generate_response import generate_content, create_prompt
from utility.speak import speech_to_text
import time
import asyncio


# Streamlit app layout
st.set_page_config(page_title="SheikhGPT", layout="centered")
st.title("🕌 SheikhGPT")


# async def text_to_speech(text, outputFilename):
#     communicate = edge_tts.Communicate(text, "en-AU-WilliamNeural")
#     await communicate.save(outputFilename)
    
# Function to handle speech-to-text input



# User input via chat or speech
col1, col2 = st.columns([3, 1])
with col1:
    user_query = st.chat_input(f"Ask any About Islam >...")
with col2:
    use_speech = st.button("🎤", help="Click to use speech input")

if use_speech:
    user_query = speech_to_text()

# Process user query
if user_query:
    # Loading indicator while generating the response
    with st.spinner('Generating Islamic content >...'):
        time.sleep(2)  # Simulate the time it takes to generate the response
        prompt = create_prompt(user_query)
        response = generate_content(prompt)  # Generate the response in chosen language
    
    # Display and speak response
    st.chat_message("user").write(user_query)
    st.chat_message("assistant").markdown(response)
    # asyncio.run(text_to_speech(response, 'response.mp3'))
    # st.audio('response.mp3')

    # Icon button for text-to-speech
    if st.button("🔊", help="Click to listen to the response"):
        pass

   