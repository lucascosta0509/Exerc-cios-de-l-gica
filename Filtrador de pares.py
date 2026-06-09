#dada certa lista de números retorne apenas os que forem pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numerosP =[]
for numero in numeros:
    resto = (numero/2) % 1
    if resto == 0:
        numerosP.append(numero)
print(f"os números pares são {numerosP}")
