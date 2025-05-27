import random
import time

# Lista de palavras
todas_palavras = ["python", "java", "javascript", "php", "sql", "kotlin", "ruby", "go", "swift", "typescript"]
palavras_jogadas = []

# Desenhos da forca
forca_ascii = [
    """
     ------
     |    |
     |
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
    _|_
    """
]

# Dificuldades
dificuldades = {
    "fácil": 10,
    "médio": 7,
    "difícil": 5
}

jogando = True

while jogando:
    inicio = ""
    while inicio != "COMEÇAR":
        inicio = input('Bem-vindo ao jogo da forca, digite "COMEÇAR" para iniciar o jogo:\n').strip().upper()
        if inicio != "COMEÇAR":
            print('Verifique se está digitando "COMEÇAR" corretamente.')

    # Selecionar dificuldade
    dificuldade = input("Escolha a dificuldade (fácil / médio / difícil):\n").strip().lower()
    tentativas = dificuldades.get(dificuldade, 5)

    # Selecionar palavra que ainda não foi usada
    palavras_restantes = list(set(todas_palavras) - set(palavras_jogadas))
    if not palavras_restantes:
        print("Todas as palavras foram jogadas! Reiniciando lista...")
        palavras_jogadas.clear()
        palavras_restantes = todas_palavras.copy()

    palavra = random.choice(palavras_restantes).upper()
    palavras_jogadas.append(palavra)

    acertos = ["_"] * len(palavra)
    erros = 0
    letras_usadas = set()
    pontos = 0
    tempo_limite = 60  # segundos
    inicio_tempo = time.time()

    print(" ".join(acertos))

    while erros < tentativas and "_" in acertos:
        # Verifica o tempo
        if time.time() - inicio_tempo > tempo_limite:
            print("⏰ Tempo esgotado!")
            break

        print(forca_ascii[erros])
        letra = input('\nDigite uma letra ou tente acertar a palavra inteira.\nDigite "DICA" para uma ajuda:\n').strip().upper()

        if not letra:
            print("Digite algo!")
            continue

        if letra == "DICA":
            print("💡 Dica: É uma linguagem de programação!")
            print(" ".join(acertos))
            continue

        if len(letra) > 1:
            if letra == palavra:
                acertos = list(palavra)
                pontos += 50
                break
            else:
                print(f"❌ Você errou a palavra! A palavra correta era: {palavra}")
                erros = tentativas
                break

        if letra in letras_usadas:
            print("Você já tentou essa letra!")
            continue

        letras_usadas.add(letra)

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    acertos[i] = letra
            pontos += 10
            print("✅ Letra correta!")
        else:
            erros += 1
            pontos = max(0, pontos - 5)
            print(f"❌ Letra errada! ({tentativas - erros} tentativas restantes)")

        print("Letras usadas:", ", ".join(sorted(letras_usadas)))
        print(" ".join(acertos))

    if "_" not in acertos:
        print("🎉 Parabéns, você venceu!")
    elif erros >= tentativas:
        print(forca_ascii[erros])
        print(f"💀 Você perdeu! A palavra era: {palavra}")

    print(f"🧮 Sua pontuação final: {pontos} pontos")

    continuar = input('Deseja jogar novamente? (S/N):\n').strip().upper()
    if continuar != "S":
        print("Jogo encerrado. Obrigado por jogar!")
        jogando = False
