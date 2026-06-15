#Crie um dicionário que funcione como um dicionário de tradução (Ex: {"red": "vermelho", "blue": "azul"}).
# Peça para o usuário digitar uma cor em inglês e exiba a tradução. Se a cor não existir no dicionário,
# exiba uma mensagem amigável dizendo que a cor não foi encontrada.
tabela = {"black":"preto","white":"branco","gray":"cinza","grey":"cinza","red":"vermelho","green":"verde","blue":"azul","yellow":"amarelo",
 "orange":"laranja","purple":"roxo","pink":"rosa","brown":"marrom"}
CorI = input("digite um nome de uma cor em inglês: ").lower()
if CorI in tabela:
    CorP = tabela.get(CorI)
    print(f"a sua cor em português é {CorP}")
else:
    print("infelizmente sua cor não foi achada")