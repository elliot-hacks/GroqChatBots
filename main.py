import os
from groq import Groq
import gradio as gr

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)




def chat(message):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": message,
        }
    ],
    model="mixtral-8x7b-32768",
    )

    return chat_completion.choices[0].message.content

demo = gr.Interface(
    fn=chat,
    inputs=["text"],
    outputs=["text"],
)

demo.launch()
