import vertexai
from vertexai.preview.language_models import TextGenerationModel
vertexai.init(project="x-avenue-425405-v4", location="us-central1")
model = TextGenerationModel.from_pretrained("text-bison@001")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = model.predict(
        prompt=user_input,
        # ... Additional parameters for temperature, max_output_tokens, etc.
    )
    print(f"Chatbot: {response.text}")

# ... (Previous code remains the same)
chat_history = []

while True:
    # ...
    response = model.predict(
        prompt=f"{''.join(chat_history)}\nYou: {user_input}",
        # ...
    )
    chat_history.append(f"You: {user_input}")
    chat_history.append(f"Chatbot: {response.text}")
    # ...


