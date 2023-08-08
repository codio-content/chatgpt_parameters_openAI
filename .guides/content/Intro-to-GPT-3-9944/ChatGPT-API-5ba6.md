
**APIs**, or Application Programming Interfaces, are incredibly useful tools that allow different software systems to communicate and interact with each other. In other words, APIs  enable integration between different systems, allowing them to share information and work together more seamlessly. Overall, APIs are a powerful and essential tool for modern software development, enabling faster innovation and greater interoperability between systems. This makes it easier and faster to build new applications, as developers can leverage existing functionality without having to reinvent the wheel. 

Developers can now integrate **ChatGPT** and **Whisper** models into their apps and products through our API. In this course, we will practice interacting with the different APIs.

|||
With the OpenAI Chat API, developers can create custom applications that leverage the powerful GPT-3.5-turbo and GPT-4 models. These applications can perform a wide range of tasks including:
* Draft an email or other piece of writing
* Write Python code
* Answer questions about a set of documents
* Create conversational agents
* Give your software a natural language interface
* Tutor in a range of subjects
* Translate languages
* Simulate characters for video games and much more

|||

The possibilities are virtually endless, and the API offers a flexible and scalable platform for building cutting-edge natural language processing applications. Try copy and pasting the following code:
```python
prompts ="Write a tagline for an ice cream shop"
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts)

print(response['choices'][0]['text'].strip())

```

{Try it!}(python3 completion.py)

{Check It!|assessment}(multiple-choice-867101325)
