from fastapi import FastAPI
from chat.chat import init_chat, send_message

app = FastAPI()

llm = init_chat()

@app.post("mealmind/classify")
def clasify_prompt(prompt: str):
    #TODO
    #call the classifier
    return prompt


@app.post("mealmind/generateMenu")
def generate_menu(menu_type: str):
    #TODO
    #call the GAN
    menu = []
    return menu

@app.post("mealmind/chat")
def chat(prompt: str):
    response = send_message(llm, prompt)
    return response


