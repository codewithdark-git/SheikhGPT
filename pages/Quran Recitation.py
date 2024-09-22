import streamlit as st
import os
from utility.recitation_quran import get_quran_recitation, merge_audio


# List of Surah names with their corresponding index
surah_list = [
    "1. Al-Fatiha", "2. Al-Baqarah", "3. Aal-E-Imran", "4. An-Nisa", "5. Al-Maidah",
    "6. Al-An'am", "7. Al-A'raf", "8. Al-Anfal", "9. At-Tawbah", "10. Yunus",
    "11. Hud", "12. Yusuf", "13. Ar-Ra'd", "14. Ibrahim", "15. Al-Hijr",
    "16. An-Nahl", "17. Al-Isra", "18. Al-Kahf", "19. Maryam", "20. Ta-Ha",
    "21. Al-Anbiya", "22. Al-Hajj", "23. Al-Mu'minun", "24. An-Nur", "25. Al-Furqan",
    "26. Ash-Shu'ara", "27. An-Naml", "28. Al-Qasas", "29. Al-Ankabut", "30. Ar-Rum",
    "31. Luqman", "32. As-Sajda", "33. Al-Ahzab", "34. Saba", "35. Fatir",
    "36. Ya-Sin", "37. As-Saffat", "38. Sad", "39. Az-Zumar", "40. Ghafir",
    "41. Fussilat", "42. Ash-Shura", "43. Az-Zukhruf", "44. Ad-Dukhan", "45. Al-Jathiya",
    "46. Al-Ahqaf", "47. Muhammad", "48. Al-Fath", "49. Al-Hujurat", "50. Qaf",
    "51. Adh-Dhariyat", "52. At-Tur", "53. An-Najm", "54. Al-Qamar", "55. Ar-Rahman",
    "56. Al-Waqia", "57. Al-Hadid", "58. Al-Mujadila", "59. Al-Hashr", "60. Al-Mumtahina",
    "61. As-Saff", "62. Al-Jumu'a", "63. Al-Munafiqun", "64. At-Taghabun", "65. At-Talaq",
    "66. At-Tahrim", "67. Al-Mulk", "68. Al-Qalam", "69. Al-Haaqqa", "70. Al-Ma'arij",
    "71. Nuh", "72. Al-Jinn", "73. Al-Muzzammil", "74. Al-Muddathir", "75. Al-Qiyama",
    "76. Al-Insan", "77. Al-Mursalat", "78. An-Naba", "79. An-Naziat", "80. Abasa",
    "81. At-Takwir", "82. Al-Infitar", "83. Al-Mutaffifin", "84. Al-Inshiqaq", "85. Al-Buruj",
    "86. At-Tariq", "87. Al-A'la", "88. Al-Ghashiya", "89. Al-Fajr", "90. Al-Balad",
    "91. Ash-Shams", "92. Al-Lail", "93. Ad-Duha", "94. Ash-Sharh", "95. At-Tin",
    "96. Al-Alaq", "97. Al-Qadr", "98. Al-Bayyina", "99. Az-Zalzalah", "100. Al-Adiyat",
    "101. Al-Qaria", "102. At-Takathur", "103. Al-Asr", "104. Al-Humazah", "105. Al-Fil",
    "106. Quraish", "107. Al-Ma'un", "108. Al-Kawthar", "109. Al-Kafirun", "110. An-Nasr",
    "111. Al-Masad", "112. Al-Ikhlas", "113. Al-Falaq", "114. An-Nas"
]


# Streamlit interface
st.subheader("Quran Recitation with Urdu Translation")

# User input for Surah and Ayat range
surah = st.sidebar.selectbox("Select Surah", surah_list)
surah_index = surah.split(".")[0]  # Extract the Surah index

from_ayah = st.sidebar.number_input("From Ayah", min_value=1, value=1)
to_ayah = st.sidebar.number_input("To Ayah", min_value=from_ayah, value=from_ayah)

# Reciter selection
reciter = st.sidebar.selectbox("Select reciter", [
    "Mishary Rashid Alafasy", 
    "Abdul Basit Murattal", 
    "Saad Al-Ghamdi", 
    "Maher Al-Muaiqly"
]) 
   

# Mapping reciter names to the API IDs
reciter_mapping = {
    "Mishary Rashid Alafasy": "ar.alafasy",
    "Abdul Basit Murattal": "ar.abdulbasitmurattal",
    "Saad Al-Ghamdi": "ar.saoodshuraym",
    "Maher Al-Muaiqly": "ar.mahermuaiqly"
    
}

# When user clicks "Play Recitation"
if st.button("Play Recitation"):
    if surah_index and from_ayah and to_ayah and reciter:
        reciter_id = reciter_mapping[reciter]  # Get the reciter ID based on the selection
        
        with st.spinner('Fetching recitation and translation...'):
            audio_urls, urdu_translation = get_quran_recitation(surah_index, from_ayah, to_ayah, reciter_id)
        
        if audio_urls and urdu_translation:
            # Merge recitation audios into one file
            with st.spinner('Merge recitation audios...'):
                recitation_file = merge_audio(audio_urls)
                st.success("Recitation combined and ready.")
            
            with st.spinner('Almost Done ....'):
                st.write("**Urdu Translation:**")
                st.code(urdu_translation, language='python', line_numbers=True)

            
                # Play combined recitation
                st.write("**Recitation Audio:**")
                st.audio(recitation_file)


        else:
            st.error("Recitation or translation not found for the selected Surah and Ayat range.")
    else:
        st.error("Please enter a valid Surah, Ayat range, and select a reciter.")
