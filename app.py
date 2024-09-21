import streamlit as st
import edge_tts
from utility.generate_response import generate_content, create_prompt
from utility.speak import speech_to_text
import time
import asyncio
import json
from deep_translator import GoogleTranslator

# Streamlit app layout
st.set_page_config(page_title="SheikhGPT", layout="centered")
st.title("🕌 SheikhGPT")

# Language settings
LANGUAGES = {
    "English": {"code": "en", "voice": "en-US-GuyNeural"},
    "Arabic": {"code": "ar", "voice": "ar-SA-HamedNeural"},
    "Urdu": {"code": "ur", "voice": "ur-PK-AsadNeural"},
    "Indonesian": {"code": "id", "voice": "id-ID-ArdiNeural"},
    "French": {"code": "fr", "voice": "fr-FR-HenriNeural"},
    "Spanish": {"code": "es", "voice": "es-ES-AlvaroNeural"},
    "Turkish": {"code": "tr", "voice": "tr-TR-AhmetNeural"},
    "Malay": {"code": "ms", "voice": "ms-MY-OsmanNeural"}
}

# Sidebar for settings
st.sidebar.title("Settings")
input_language = st.sidebar.selectbox("Select Input Language", list(LANGUAGES.keys()))
output_language = st.sidebar.selectbox("Select Output Language", list(LANGUAGES.keys()))

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'favorites' not in st.session_state:
    st.session_state.favorites = []
if 'show_favorite' not in st.session_state:
    st.session_state.show_favorite = None

# Asynchronous text-to-speech function
async def text_to_speech(text, output_file, voice):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)

# Translate text
def translate_text(text, src_lang, dest_lang):
    if src_lang == dest_lang:
        return text
    translator = GoogleTranslator(source=LANGUAGES[src_lang]['code'], target=LANGUAGES[dest_lang]['code'])
    return translator.translate(text)

# User input via chat or speech
col1, col2 = st.columns([3, 1])
with col1:
    user_query = st.chat_input(f"Ask anything about Islam in {input_language}...")
with col2:
    use_speech = st.button("🎤", help=f"Click to use speech input in {input_language}")

if use_speech:
    with st.spinner(f"Listening in {input_language}..."):
        user_query = speech_to_text(language=LANGUAGES[input_language]['code'])

# Process user query
if user_query:
    try:
        # Translate user query to English for processing
        english_query = translate_text(user_query, input_language, "English")
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_query, "language": input_language})
        
        # Loading indicator while generating the response
        with st.spinner('Generating Islamic content...'):
            prompt = create_prompt(english_query, "English")
            english_response = generate_content(prompt)
        
        # Translate response to output language
        response = translate_text(english_response, "English", output_language)
        
        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": response, "language": output_language})
        
        # Generate and play audio response
        output_file = "response.mp3"
        asyncio.run(text_to_speech(response, output_file, LANGUAGES[output_language]['voice']))
        st.audio(output_file)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Display chat history
for idx, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(f"**{message['language']}:** {message['content']}")
    
    # Add favorite button for assistant messages
    if message["role"] == "assistant":
        if st.button("⭐", key=f"fav_{idx}"):
            st.session_state.favorites.append(message)
            st.success("Added to favorites!")

# Sidebar for favorites
st.sidebar.title("Favorites")
for i, fav in enumerate(st.session_state.favorites):
    if st.sidebar.button(f"Favorite {i+1} ({fav['language']})", key=f"fav_button_{i}"):
        st.session_state.show_favorite = i

# Display selected favorite
if st.session_state.show_favorite is not None:
    fav = st.session_state.favorites[st.session_state.show_favorite]
    st.sidebar.text_area("Selected Favorite", fav['content'], height=150)
    if st.sidebar.button("Hide Favorite"):
        st.session_state.show_favorite = None

# Export chat history
if st.sidebar.button("Export Chat History"):
    chat_history = json.dumps(st.session_state.messages, indent=2, ensure_ascii=False)
    st.sidebar.download_button(
        label="Download JSON",
        data=chat_history,
        file_name="sheikgpt_chat_history.json",
        mime="application/json"
    )

# Clear chat history
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = []
    st.rerun()

# Clear favorites
if st.sidebar.button("Clear Favorites"):
    st.session_state.favorites = []
    st.session_state.show_favorite = None
    st.rerun()