# Configuração da API
openai.api_key = "SUA_CHAVE_API"

def chat_ia(pergunta):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": pergunta}]
    )
    return resposta["choices"][0]["message"]["content"]

# Loop de interação com o usuário
print("Chat IA - Digite 'sair' para encerrar.")
while True:
    user_input = input("Você: ")
    if user_input.lower() == "sair":
        break
    resposta = chat_ia(user_input)
    print("IA:", resposta)
