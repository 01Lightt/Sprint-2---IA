import openai

openai.api_key = "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"

def chatsanofi(prompt):
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo-16k",
        messages = [{"role": "user","content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair","voltar", "tchau"]:
            break

        response = chatsanofi(user_input)
        print("SanofiBot: ", response)
