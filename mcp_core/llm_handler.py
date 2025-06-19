# Uses OpenAI to generate a reply based on conversation history

#import openai
import os

#put key here

def generate_reply(conversation):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=conversation
    )
    return response.choices[0].message.content

