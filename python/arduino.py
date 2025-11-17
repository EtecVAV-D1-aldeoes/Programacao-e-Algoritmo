import random

# Lista de perguntas com alternativas e a resposta correta
questoes = [
    {
        "pergunta": "1. Qual é a capital do Brasil?",
        "alternativas": {
            "A": "São Paulo",
            "B": "Brasília",
            "C": "Rio de Janeiro",
            "D": "Salvador",
            "E": "Belo Horizonte"
        },
        "correta": "B"
    },
    {
        "pergunta": "2. Quanto é 7 x 8?",
        "alternativas": {
            "A": "54",
            "B": "56",
            "C": "58",
            "D": "60",
            "E": "52"
        },
        "correta": "B"
    },
    {
        "pergunta": "3. Quem escreveu 'Dom Casmurro'?",
        "alternativas": {
            "A": "Machado de Assis",
            "B": "José de Alencar",
            "C": "Clarice Lispector",
            "D": "Graciliano Ramos",
            "E": "Monteiro Lobato"
        },
        "correta": "A"
    },
]

# Gerar até 50 questões (duplicando as de exemplo só para preencher)
while len(questoes) < 50:
    nova = questoes[len(questoes) % 3].copy()
    nova["pergunta"] = f"{len(questoes)+1}. {nova['pergunta'].split('. ', 1)[1]}"
    questoes.append(nova)

# Início do quiz
print("=== QUIZ DE 50 QUESTÕES ===\n")

for q in questoes:
    print(q["pergunta"])

    # Embaralhar as alternativas
    letras = list(q["alternativas"].keys())
    random.shuffle(letras)

    # Mostrar as alternativas embaralhadas
    for letra in letras:
        print(f"{letra}) {q['alternativas'][letra]}")

    # Ler resposta do usuário
    resposta = input("Sua resposta: ").strip().upper()

    # Verificar resposta
    if resposta == q["correta"]:
        print("✅ Resposta certa!\n")
    else:
        print("❌ Você errou!\n")
        break  # encerra o quiz se errar
else:
    print("🎉 Parabéns! Você acertou todas as 50 questões!")
