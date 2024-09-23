import streamlit as st
from utility.generate_response import generate_content  # Your LLM function

# Function to fetch Hadith using LLM
def fetch_hadith_llm(query):
    prompt = f"""Provide at least five Hadiths in Arabic related to the topic '{query}', 
        followed by their Urdu translations, and include the reference for each (book name, volume, and hadith number). 
        Please keep the response limited to the Hadiths, translations, and references only."""
    hadith_response = generate_content(prompt)  # LLM response
    return hadith_response

# Streamlit layout for Hadith search
st.title("Hadith Search")

st.write('Choose Your Choice 🪧:')
col1, col2, col3 = st.columns(3)
with col1:
    if st.button('Back To Home'):
        st.switch_page("app.py")
with col2:
    if st.button('SheikhGPT'):
        st.switch_page("pages/SheikhGPT.py")
with col3:
    if st.button('Recitation Quran'):
        st.switch_page("pages/Quran Recitation.py")


st.markdown("----")

st.chat_message('ai').write("📜 A-Salam ul Kom! Welcome to the Hadith search. Type a topic, and I'll provide you with authentic Hadiths along with translations and references!")


user_query = st.text_input("Enter your Hadith query (e.g., prayer, fasting)")

# Fetch and display Hadith
if st.button("Fetch Hadith"):
    with st.spinner("Fetching Hadith..."):
        hadith_response = fetch_hadith_llm(user_query)
    
    if hadith_response:
        # Display the full Hadith response
        st.subheader("Hadiths and Translations:")
        st.write(hadith_response.strip())
    else: 
        st.error("Hadith not found or invalid query.")
