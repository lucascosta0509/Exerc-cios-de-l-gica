#Peça para o usuário digitar uma frase longa. O seu programa deve contar quantas palavras únicas (sem repetir nenhuma) existem na frase.
frase = input("digite uma frase longa: ")
fraseP = frase.split()
palavrasNR = set()
palavrasR = set()
for palavra in fraseP:
    if palavra not in palavrasNR:
        palavrasNR.add(palavra)
    elif palavra in palavrasNR:
        palavrasR.add(palavra)
nr = palavrasNR - palavrasR
qnr = len(nr)
print(f"{qnr} palavras não possuem repetição na frase sendo elas: {nr}")
