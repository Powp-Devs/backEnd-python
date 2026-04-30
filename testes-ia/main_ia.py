#from ai_assistent import ERPAssistent
#from ai_assistent2 import ERPAssistent
from ai_assistent3 import ERPAssistent

bot = ERPAssistent()

print("Assistente ERP iniciando...")
print("Digite 'sair' para encerrar.\n")

while True: 

    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        break

    resposta = bot.perguntar(pergunta)

    print("\nAssistente:")
    print(resposta)
    print()