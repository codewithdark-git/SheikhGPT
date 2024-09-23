from g4f.client import Client

# Define function for generate content
def generate_content(prompt):
    client = Client()   
    response = client.chat.completions.create(
        model='gpt-4o',
        messages =[{'role': 'user', 'content': prompt}]

    )

    response = response.choices[0].message.content
    return response
   


def create_prompt(user_query, language):
    prompt = f"""You are an AI trained in Islamic teachings. Provide a concise yet informative response to the 
        following question based on Islamic teachings:
        {user_query}
        In this specific language:
        {language}

        Your response should:
        1. Be approximately 10 lines long.
        2. Focus on key points from the Quran, Hadith, or respected Islamic scholars.
        3. When quoting the Quran or Hadith, clearly format it with respect, using quotation marks and separating it from the rest of the text. Ensure the verse or Hadith reference is presented in a distinct format (e.g., bold or italic).
        4. Include at least one direct reference to the Quran or Hadith if applicable.
        5. Avoid general or vague statements.
        6. Present the most widely accepted view in Islamic scholarship.

        Emphasize accuracy and relevance in your concise answer, and ensure any Quranic or Hadith quotes are presented in the most respectful and clear manner."""


    return prompt

