import streamlit as st

st.set_page_config(page_title="SheikhGPT", layout="centered")

# Title of the app
st.title("Welcome to SheikhGPT")


st.write('Choose Your Choice 🪧:')
col1, col2, col3 = st.columns(3)
with col1:
    if st.button('SheikhGPT'):
        st.switch_page("pages/SheikhGPT.py")
with col2:
    if st.button('Recitation Quran'):
        st.switch_page("pages/Quran Recitation.py")
with col3:
    if st.button('See Hadith'):
        st.switch_page("pages/Hadith.py")

st.markdown("----")

# Main content with product description
st.markdown("""
## **About SheikhGPT**

**SheikhGPT** is your personal AI-based Islamic assistant designed to provide an interactive and enriching experience in exploring Islamic teachings. The app supports Quran recitations, Hadith retrieval, and generating content related to various Islamic topics. Whether you're looking to listen to Quranic verses, learn from Hadith, or ask questions about Islam, SheikhGPT is here to assist you.

### **Core Features**
1. **Quran Recitation**: Choose any Surah and Ayat range to listen to Quranic verses, along with an Urdu translation. You can also select from various renowned reciters.
2. **Hadith Retrieval**: Search for Hadiths on specific topics. The app provides Hadiths in Arabic with Urdu translations and references for authenticity.
3. **Islamic Content Generation**: Using AI, SheikhGPT can generate responses to your Islamic questions in your selected language, making it easy to learn more about Islam.

---

## **How to Use SheikhGPT**

### **1. Quran Recitation**
- **Step 1**: Navigate to the **Quran Recitation** page.
- **Step 2**: Choose the Surah from the dropdown list, select the Ayat range, and choose your favorite reciter.
- **Step 3**: Click the "Play Recitation" button to listen to the Quran along with Urdu translation.

### **2. Hadith Retrieval**
- **Step 1**: Go to the **Hadith** section.
- **Step 2**: Enter a query such as "prayer" or "fasting."
- **Step 3**: Click "Fetch Hadith" to retrieve relevant Hadiths along with Arabic text, Urdu translation, and references.

### **3. Ask Questions**
- **Step 1**: In the chat interface on the main page, type your Islamic question in your chosen language.
- **Step 2**: You can also use speech input by clicking the 🎤 button.
- **Step 3**: The AI will generate a response, which will be translated into the selected language.
- **Step 4**: Mark the responses as favorites for future reference.

---

## **Additional Features**

### **1. Favorites**
- You can save any responses or content by marking them as favorites using the ⭐ button. 
- Access your favorite responses anytime from the sidebar under the "Favorites" section.

 ### **2. Multilingual Support**
- Choose your **input and output language** from the **Settings** in the sidebar. This feature allows users to ask questions in their preferred language, and receive responses translated accurately.

### **3. Export Chat History**
- Save your chat history by clicking the "Export Chat History" button in the sidebar, and download it as a JSON file.

### **4. Clear Data**
- Use the **Clear Chat History** and **Clear Favorites** buttons to reset the app and start fresh.

---

## **More About the App**

**SheikhGPT** is built to simplify access to Islamic content in an easy-to-use interface. Whether you're a student of Islamic knowledge or just someone curious about certain topics, SheikhGPT offers a user-friendly platform to help you explore. With AI-driven responses, recitations, and Hadiths, the app covers a wide array of Islamic topics and provides authentic references to deepen your understanding.
""")