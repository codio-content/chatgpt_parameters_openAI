When you use the OpenAI ChatGPT API, you'll need to provide a list of messages that represent a conversation. Each message has two pieces of information: who said it (either the "system," the "user," or the "assistant") and what they said. You can have as few or as many messages as you want in a conversation. We will cover the format for API calls, explanations, and a new example for you to try.
```
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a financial advisor."},
        {"role": "user", "content": "What are some tips for saving money?"},
        {"role": "assistant", "content": "Creating a budget, reducing expenses, and saving on utilities are some ways to save money."},
        {"role": "user", "content": "How do I create a budget?"}
    ]
)


print(response['choices'][0]['message']['content'].strip())
```

{Try It!}(python3 temp2.py)
Usually, a conversation starts with a message from the system, followed by alternating messages from the user and the assistant. The system message sets the behavior of the assistant, while user messages serve as prompts for the assistant's response.

The system message tells the assistant what it should do. For example, you could start with "You are a helpful assistant" as in our previous prompt. In this example, the conversation starts with a system message, setting the role of the AI as a financial advisor. 

The user messages give instructions to the assistant. They can be written by end users or set by a developer. In our case, the user then asks for tips on saving money.

The assistant responds with a few general suggestions. Finally, the user asks for more information on creating a budget. This API call will generate a response from the AI, providing guidance on budget creation.

The assistant messages keep track of previous responses. They can also be written by a developer to give examples of desired behavior. Make sure to include the open and closing brackets for the list of messages.
```
 messages=[
        {"role": "system", "content": "You are a financial advisor."},
        {"role": "user", "content": "What are some tips for saving money?"},
        {"role": "assistant", "content": "Creating a budget, reducing expenses, and saving on utilities are some ways to save money."},
        {"role": "user", "content": "How do I create a budget?"}
    ]
```

{Try It!}(python3 temp2.py 20)
It's important to include the entire conversation history if you want to refer to previous messages later on. The models used by the API have no memory of past requests, so all relevant information must be supplied via the conversation. If the conversation is too long for the model to handle, it may need to be shortened in some way. (cannot fit within the model’s token limit).

{Check It!|assessment}(multiple-choice-1607862764)
