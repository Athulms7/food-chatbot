import gradio
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv('GROQ_API_KEY', "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"))

def initialize_messages():
    return [{"role": "system",
             "content": "You are a certified nutritionist and culinary expert with deep knowledge of food science, dietary needs, and global cuisines. Your role is to assist users by providing accurate nutritional information, healthy meal suggestions, and step-by-step recipes. Always answer clearly, professionally, and in a helpful tone, tailored to the user's dietary preferences or goals."}]

messages_prmt = initialize_messages()

def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama3-8b-8192",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply

iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me about food nutrients or recipes"),
                     title="Food & Recipe Chatbot",
                     description="Chat bot for nutrition facts and cooking tips",
                     theme="soft",
                     examples=["hi","What are the nutrients rich foods", "Give me a recipe using egg"],
                     submit_btn=True
                     )

if __name__ == "__main__":
    iface.launch(share=True)
