from random import choice

print("|" + "Mission Maker".center(30) + "|")
print()
print("Condições atendidas, a missão: (A vontade do fraco) foi criada")
esq = input("Você aceita \n[1] - Sim \n[2] - Não \n: ")

missoes = ["Praticar Seu inglês", "Desenhar um personagem", "Crie um programa"]
recompensas = ["Doce", "Pizza", "Suco"]
punicoes = ["Sem internet por 1h", "Sem jogos por 1d", "Sem youtube/Tiktok por 1 semana"]

r = choice(missoes)
print(f"Nova Quest: {r}")
print()

esq = int(input("Você completou a missão? \n[1] - Sim \n[2] - Não \n: "))
if esq == 1:
    print("Parabéns Jogador, veja suas recompensas:\n")
    print(choice(recompensas))
else:
    print("Você Falhou, sua punição será: \n")
    print(choice(punicoes))

