#Dado o dicionário tradutor = {"apple": "maçã", "banana": "banana", "grape": "uva"},
#crie um código que gere um novo dicionário invertido, onde o português vira a chave e o inglês vira o valor. Ex: {"maçã": "apple", ...}
tradutor = {"apple": "maçã", "banana": "banana", "grape": "uva"}
portugues = []
ingles = []
for item in tradutor:
    ingles.append(item)
    dados = tradutor.get(item)
    portugues.append(dados)
tradutorI = {}
for i in range(len(tradutor)):
    p = portugues[i]
    i = ingles[i]
    tradutorI.setdefault(p,i)
print(tradutorI)


    
    
