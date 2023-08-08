import os
import openai
import secret
openai.api_key=secret.api_key

# CODIO SOLUTION BEGIN

response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  max_tokens=25,
  temperature=1,
  messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Provide some healthy food options"}
    ],
  n=6
)

print(response["choices"][3]["message"]["content"].replace("1. ", ""))
# CODIO SOLUTION END