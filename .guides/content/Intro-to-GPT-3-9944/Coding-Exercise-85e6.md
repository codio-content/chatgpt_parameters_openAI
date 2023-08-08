Requirement :
* Write a code so that we have the most random possible answer. Meaning setting the value that determines randomness to max
* Generate 6 responses 
* The completion token limit should be set 25
* Do not include any argument that are not necessary to the requirements

{Try it!}(python3 ktest1.py)

{Check It!|assessment}(test-425491894)
|||guidance
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  max_tokens=25,
  temperature=2,
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Provide some healthy food options"}
    ],
  n=6
)

print(response["choices"][4]["message"]["content"])
|||