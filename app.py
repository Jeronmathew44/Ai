
import openai

# Set up the OpenAI API client
openai.api_key = "YOUR_API_KEY"

# Define the prompt for the language model
prompt = "Generate a short story about a group of friends who go on an adventure to find a hidden treasure."

# Generate the story using the language model
response = openai.Completion.create(
    prompt=prompt,
    engine="text-bison-001",
    max_tokens=1024,
    temperature=0.7,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

# Print the generated story
print(response.choices[0].text)
