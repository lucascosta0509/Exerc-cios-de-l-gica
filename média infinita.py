#Crie um programa que fique pedindo números inteiros para o usuário infinitamente. Quando o usuário digitar -1,
#  o programa para e exibe a média de todos os números digitados (sem contar o -1).
func = True
numeros = []
while func == True:
    numero = int(input("digite um número"))
    if numero == -1:
        func = False
    else:
        numeros.append(numero)
numerosT = sum(numeros)/len(numeros)
print(numerosT)
    