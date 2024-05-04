from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler


while True:
    user_input = input("Your question: ")

    if user_input.strip().lower() == 'out':
        print("Thanks for using our chat. Bye!")
        break

    response = llm.invoke(user_input)

    print("Response:", response)
def init_chat():
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

    llm = LlamaCpp(
        model_path="llama-2-7b-chat.Q4_K_M.gguf",
        temperature=0.75,
        max_tokens=2000,
        top_p=1,
        callback_manager=callback_manager,
        verbose=True, 
    )
    print("----------------------------------------------------")
    print("Welcome to the 'MealMind' chat! (Type 'out' to exit)")

    return llm
def send_message(llm, prompt):
    response = llm.invoke(prompt)
    return response

