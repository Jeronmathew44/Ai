# bot.py
from config import Config
import openai
import os

# Load environment variables
openai.api_key = Config.OPENAI_API_KEY
api_hash = Config.API_HASH
api_id = Config.API_ID
bot_token = Config.BOT_TOKEN

# Plain text example
greeting = "Hello! Type 'exit' to end the conversation."

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        n=1,
    )
    return response.choices[0].text.strip()

def main():
    print(f"ChatGPT Bot: {greeting}")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("ChatGPT Bot: Goodbye!")
            break
        
        prompt = f"You: {user_input}\nChatGPT Bot:"
        bot_response = chat_with_gpt(prompt)
        
        print(f"ChatGPT Bot: {bot_response}")

if __name__ == "__main__":
    main()
