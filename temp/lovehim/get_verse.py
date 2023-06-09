import openai
import argparse

# Set up the OpenAI API key
openai.api_key = "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"

# Define the function to generate a Bible verse based on a topic
def generate_verse(topic):
    prompt = f"Generate a Bible verse about {topic}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
        presence_penalty=0.5,
    )
    verse = response.choices[0].text.strip()
    return verse

# Parse the command-line arguments
parser = argparse.ArgumentParser(description='Get a Bible verse based on a topic')
parser.add_argument('topic', type=str, help='the topic you want the verse to be about')

args = parser.parse_args()

# Call the generate_verse function with the user-specified topic
verse = generate_verse(args.topic)

# Print out the resulting Bible verse
print(verse)
