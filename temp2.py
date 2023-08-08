import os
import openai
import secret
openai.api_key=secret.api_key
### CODIO SOLUTION BEGIN
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's a good book to read on a rainy day?"}
    ],
  n=3
)

print(response)
### CODIO SOLUTION END