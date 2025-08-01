from g4f.client import Client

client = Client()

while True:
    text = input('me: ')
    response = client.chat.completions.create(
        model="Copilot",
        messages=[{"role": "user", "content": text}],
        web_search=False
    )
    print('AI: ', response.choices[0].message.content)