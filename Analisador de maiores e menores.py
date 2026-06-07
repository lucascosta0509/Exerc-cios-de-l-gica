numeros = [12, 45, 2, 89, 34, 21, 0, -5, 66]
maior_numero = 0
menor_numero = 0
for numero in numeros:
    if numero < menor_numero:
        menor_numero = numero
    elif numero > maior_numero:
        maior_numero = numero
print(f"o menor número é {menor_numero}")
print(f"o maior número é {maior_numero}")