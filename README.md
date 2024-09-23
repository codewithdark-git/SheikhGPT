# **SheikhGPT **

Welcome to **SheikhGPT**, a Streamlit-powered Islamic content generation tool. The app allows users to interact with Islamic teachings through Quran recitations, Hadith retrieval, and custom Islamic content generation.

## **1. Overview**

SheikhGPT provides three main functionalities:
- **Quran Recitation**: Listen to Quran recitations in Arabic with Urdu translation.
- **Hadith Retrieval**: Search for Hadiths by topics, with Arabic and Urdu translations, and references.
- **Islamic Content Generation**: Ask Islamic questions and receive answers in your chosen language.

## **2. App Structure**

The app is divided into several sections:

### **2.1 Main Page**
- **Title**: Displays "SheikhGPT" with an icon.
- **Navigation Links**:
  - **Quran Recitation**: Directs users to the Quran recitation section.
  - **Hadith**: Allows users to search for Hadiths.

### **2.2 Sidebar**
- **Language Selection**: Choose your input and output language for the content generation.
- **Settings**: Manage and review your favorite responses and export your chat history.
  
### **2.3 Chat Interface**
- **Text Input**: Users can type their Islamic questions here.
- **Speech Input**: Click the microphone button to ask your question using speech recognition.
- **Generated Responses**: SheikhGPT will answer your question using its language model.

### **2.4 Favorites**
- **Add to Favorites**: Users can mark responses as favorites and manage them from the sidebar.
- **View Favorites**: Users can expand a list of favorite responses in the sidebar.

## **3. Features**

### **3.1 Quran Recitation**
**How to Use:**
1. Navigate to the **Quran Recitation** page from the home screen.
2. Select a **Surah** from the dropdown list.
3. Specify the **Ayah range** (start and end Ayahs).
4. Choose your preferred **reciter** from the dropdown.
5. Click **Play Recitation**. The app will fetch the Quran recitation in Arabic along with its Urdu translation.
6. The recitation will play in the app's audio player, and the Urdu translation will be displayed.

### **3.2 Hadith Retrieval**
**How to Use:**
1. Navigate to the **Hadith** section.
2. Enter a query like "prayer" or "fasting."
3. Click **Fetch Hadith**.
4. The app will return at least five Hadiths in Arabic with Urdu translations, alongside references.

### **3.3 Islamic Content Generation**
**How to Use:**
1. Type your Islamic question in the chat input (or use speech-to-text).
2. SheikhGPT will translate your question into English, process it, and generate a response.
3. The response will be translated back into your chosen language (from the settings sidebar) and displayed.
4. Mark any response as a **Favorite** using the star button for quick access later.

## **4. Additional Features**

### **4.1 Export Chat History**
- Users can download the chat history in JSON format using the **Export Chat History** button in the sidebar.

### **4.2 Clear Data**
- Clear the chat history or your favorites using the respective buttons in the sidebar.

## **5. Error Handling**
If you encounter any issues, such as a missing recitation or invalid input, appropriate error messages will be displayed. Check if the inputs (Surah, Ayah range, and reciter) are correct, and try again.
