
import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega a chave da API
load_dotenv()

# Cria o cliente
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# Função responsável pela tradução
def traduzir(texto, idioma):

    prompt = f"Traduza para {idioma} o seguinte texto: {texto}"

    resposta = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        max_output_tokens=500
    )

    return resposta.output_text


# Programa principal
texto = input("Digite o texto: ")
idioma = input("Idioma de destino: ")

traducao = traduzir(texto, idioma)

print("\nTradução:\n")
print(traducao)
