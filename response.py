from openai import OpenAI
client = OpenAI(base_url="<your_base_url>",
                 api_key="<your_api_key>")

def token(messages, model):

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are an intelligent assistant specialized in summarization. Answer the question in detailed."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": messages
                    },
                ]
            }
        ],
        stream=True
    )

    for chunk in response:
        if chunk.choices[0].delta.content:
             yield chunk.choices[0].delta.content

