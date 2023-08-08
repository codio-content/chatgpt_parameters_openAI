### CODIO SOLUTION BEGIN
import os
import openai
import secret
openai.api_key=secret.api_key

response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "can you write me a sentece obout animal behavior."}
    ]
)


print(response['choices'][0]['message']['content'].strip())
## CODIO SOLUTION END