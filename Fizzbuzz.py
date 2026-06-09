#Objetivo: Faça um loop que conte de 1 a 30, Se o número for divisível por 3, imprima "Fizz", Se for divisível por 5, imprima "Buzz",
#  Se for divisível por 3 e por 5 ao mesmo tempo, imprima "FizzBuzz", Caso contrário, imprima o próprio número.
quantidade = 0
for i in range(1, 31):
    quantidade = quantidade+1
    resto1 = (quantidade/15) % 1
    resto2 = (quantidade/5) % 1
    resto3 = (quantidade/3) % 1
    if resto1 == 0:
        print("fizzbuzz")
    elif resto2 == 0 :
        print("buzz")
    elif resto3 == 0:
        print("fizz")
    else:
        print(quantidade)