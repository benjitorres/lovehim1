import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load the OpenAI API key from the .env file
openai.api_key = st.secrets.secrets["OPENAI_API_KEY"]


# Define the function to generate a Bible verse based on a topic
def generate_verse(topic):
    prompt = f"Generate a Bible verse about {topic}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
        presence_penalty=0.5,
    )
    verse = response.choices[0].text.strip()
    return verse

def main():
    st.title("lovehim")
    topic = st.text_input("What's on your mind?")
    if st.button("Find Verse"):
        verse = generate_verse(topic)
        st.write(verse)

if __name__ == '__main__':
    main()