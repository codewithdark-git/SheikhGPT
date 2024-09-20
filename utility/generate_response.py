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
   


def create_prompt(user_query):
    prompt = f"""
    You are an AI trained in Islamic teachings, and your responses should be based on the Quran, Hadith, and Islamic scholars. 
    Please provide a detailed and accurate response for the following question based on Islamic teachings:
    {user_query}
    
    
    Focus on presenting the answer according to Islamic sources, including references to the Quran and Hadith if applicable. Avoid general or vague answers.
    """

    return prompt

