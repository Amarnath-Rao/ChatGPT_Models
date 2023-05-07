import openai

openai.api_key =  'API_KEY'

completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": "What is freedom "}])
print(completion.choices[0].message.content)