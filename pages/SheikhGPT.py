import streamlit as st
from utility.generate_response import generate_content, create_prompt
from utility.speak import speech_to_text, text_to_speech
from utility.translate import LANGUAGES, translate_text
import time
import json
import asyncio

# Streamlit app layout
st.set_page_config(page_title="SheikhGPT", layout="centered")
st.title("🕌 SheikhGPT")

st.page_link('pages/Quran Recitation.py', icon='📖', label='Quran Recitation', help='Listen Quran recitation') 
st.page_link('pages/Hadith.py', icon='📖', label='See Your favorite Hadith') 

# Sidebar for settings
st.sidebar.title("Settings")
input_language = st.sidebar.selectbox("Select Language", list(LANGUAGES.keys()), help='Select language Input & Output Language')
output_language = input_language

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'favorites' not in st.session_state:
    st.session_state.favorites = []
if 'show_favorite' not in st.session_state:
    st.session_state.show_favorite = None

# User input via chat or speech
col1, col2 = st.columns([3, 1])
with col1:
    user_query = st.chat_input(f"Ask anything about Islam in {input_language}...")
with col2:
    use_speech = st.button("🎤", help=f"Click to use speech input in {input_language}")

if use_speech:
    with st.spinner(f"Listening in {input_language}..."):
        user_query = speech_to_text(language=LANGUAGES[input_language]['code'])

st.chat_message('ai').write('A-Salam ul Kom')

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
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Display chat history (reversed order)
for idx, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(f"{message['content']}")
        
        # Add favorite button for assistant messages
        if message["role"] == "assistant":
            is_favorite = message in st.session_state.favorites
            if st.button("⭐" if not is_favorite else "★", key=f"fav_{idx}"):
                if is_favorite:
                    st.session_state.favorites.remove(message)
                    st.success("Removed from favorites!")
                else:
                    st.session_state.favorites.append(message)
                    st.success("Added to favorites!")
                st.rerun()

# Display selected favorite
if st.session_state.show_favorite is not None:
    if 0 <= st.session_state.show_favorite < len(st.session_state.favorites):
        fav = st.session_state.favorites[st.session_state.show_favorite]
        st.markdown(fav['content'])
        if st.button("Hide Favorite"):
            st.session_state.show_favorite = None
    else:
        st.session_state.show_favorite = None
        st.rerun()

# Sidebar for favorites
st.sidebar.title("Favorites")
for i, fav in enumerate(st.session_state.favorites):
    with st.sidebar.expander(f"Favorite {i+1} ({fav['language']})"):
        st.write(fav['content'][:100] + "...")  # Show a preview
        if st.button("Remove", key=f"remove_fav_{i}"):
            st.session_state.favorites.pop(i)
            if st.session_state.show_favorite is not None and st.session_state.show_favorite >= i:
                st.session_state.show_favorite = max(0, st.session_state.show_favorite - 1)
            st.rerun()
        if st.button("View", key=f"view_fav_{i}"):
            st.session_state.show_favorite = i

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
