from ollama import chat
from apps_automatizados.spotfy import pesquisar_musica

MODELO = "llama3.2"


def perguntar_ollama(texto):
    resposta = chat(
        model=MODELO,
        messages=[
            {
                "role": "user",
                "content": texto
            }
        ]
    )

    return resposta["message"]["content"]


print("Assistente Ollama iniciado!")
print("Digite 'sair' para fechar.\n")

while True:
    comando = input("Você: ")

    if comando.lower() == "sair":
        print("Encerrando...")
        break

    resposta = perguntar_ollama(comando)

    print("\nOllama:", resposta)
    print()
    if comando == 'spotify' or 'sp':
        pesquisar_musica()