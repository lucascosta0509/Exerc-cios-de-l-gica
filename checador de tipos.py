#Dada a lista dados = [10, "vinte", 30, "quarenta", 50], faça um loop que tente somar todos os números.soma correta no final deve ser 90)
dados = [10, "vinte", 30, "quarenta", 50]
dadosN = []
for item in dados:
    if type(item) == int:
        dadosN.append(item)
print(sum(dadosN))
