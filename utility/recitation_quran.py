import requests
from pydub import AudioSegment
import io

def get_quran_recitation(surah, from_ayah, to_ayah, reciter_id):
    """
    Function to fetch the recitation audio of specific Ayat by a particular reciter.
    
    :param surah: The specific Surah number.
    :param from_ayah: The starting Ayah.
    :param to_ayah: The ending Ayah.
    :param reciter_id: The reciter's ID (based on AlQuran API reciter IDs).
    :return: Audio URL of the recitation and Urdu translation text, or None if not available.
    """
    audio_urls = []
    urdu_translation = ""
    
    for ayah in range(from_ayah, to_ayah + 1):
        # API endpoint for recitation and translation
        recitation_api_url = f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}/editions/{reciter_id}"
        translation_api_url = f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}/editions/ur.junagarhi"

        # Get recitation
        recitation_response = requests.get(recitation_api_url)
        recitation_data = recitation_response.json()

        # Get translation
        translation_response = requests.get(translation_api_url)
        translation_data = translation_response.json()

        if recitation_data['status'] == "OK" and translation_data['status'] == "OK":
            audio_urls.append(recitation_data['data'][0]['audio'])
            urdu_translation += f"Ayah {ayah}: {translation_data['data'][0]['text']}\n\n"
        else:
            return None, None
    
    return audio_urls, urdu_translation

# Function to merge audio files into one
def merge_audio(audio_urls, output_file="recitation_combined.mp3"):
    combined = AudioSegment.empty()

    # Download and combine each audio file
    for url in audio_urls:
        audio_data = requests.get(url).content
        temp_audio = AudioSegment.from_file(io.BytesIO(audio_data), format="mp3")
        combined += temp_audio

    combined.export(output_file, format="mp3")
    return output_file


