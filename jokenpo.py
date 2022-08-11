import random

#Irá definir as escolhas dos dois jogadores.
def escolhas_jogadores():
    escolha_jogador = input(f"Digite Pedra, Papel Ou Tesoura ")
    alternativas = ["pedra", "papel", "tesoura"]
    escolha_computador = random.choice(alternativas)
    escolha = {"jogador" : escolha_jogador, "computador" : escolha_computador}
    return escolha

#Irá checar as escolhas e definir o resultado do jogo.
def checagem(jogador, computador):
    print(f"Você escolheu {jogador} e o computador escolheu {computador}")
    if jogador == computador:
        return "É um empate!"
    elif jogador == "pedra":
        if computador == "tesoura":
            return "Pedra ganha de tesoura. Você venceu!"
        else:
            return "Pedra perde para papel. Você perdeu."
    elif jogador == "papel":
        if computador == "pedra":
            return "Papel ganha de pedra. Você venceu!"
        else:
            return "Papel perde para tesoura. Você perdeu."
    elif jogador == "tesoura":
        if computador == "papel":
            return "Tesoura ganha de papel. Você venceu!"
        else:
            return "Tesoura perde para pedra. Você perdeu."

#Chamada das funções

escolha = escolhas_jogadores()
resultado = checagem(escolha["jogador"], escolha["computador"])
print(resultado) 