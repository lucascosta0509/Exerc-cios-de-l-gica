#Crie um programa com um loop while que simule um caixa de mercado. O usuário vai digitando os valores dos produtos.
# Se ele digitar 0, o programa para, exibe o valor total da compra e pergunta a forma de pagamento
# (1 - Dinheiro / 2 - Cartão). Se for dinheiro, peça o valor pago e calcule o troco.
func = True
total = []
print("programa iniciado, para encerrar compra digite 0")
while func == True:
    valor = int(input("digite o valor do produto:"))
    total.append(valor)
    if valor == 0:
        func = False
total = sum(total)
print(f"o total deu {total},qual a forma de pagamento?")
resposta = int(input("digite 1 para dinheiro e 2 para cartão: "))
if resposta == 1:
    valor = int(input("digite o valor que você entregará: "))
    if valor > total:
        troco = valor - total
        print(f"seu troco foi de {troco} reais")
    elif valor == total:
        print("não houve troco") 
    elif valor < total:
        divida = total - valor
        print(f"você ainda está devendo {divida} reais")
elif resposta == 2:
    print("passe o cartão\n.\n.\n.\n.\ncompra realizada com sucesso")
