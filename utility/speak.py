import speech_recognition as sr  # For speech-to-text
import streamlit as st


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("🎤 Listening >...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            # st.write(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")
    return ""