#  Você tem um dicionário de produtos: produtos = {"Mouse": 150, "Teclado": 250, "Monitor": 900, "Fone": 80].
#  Peça para o usuário digitar um valor máximo (Ex: 200). O programa deve exibir apenas
#  os produtos que custam menos ou igual ao valor digitado.
produtos = {"Mouse": 150, "Teclado": 250, "Monitor": 900, "Fone": 80}
len(produtos)
produtosR = []
q = int(input("digite a quantidade: "))
for item in produtos:
    qp = produtos.get(item)
    if qp <= q:
        produtosR.append(item)
print(f"os produtos que estão dentro do limite estabelecido são {produtosR}")