vogais = ["a", "á", "à", "ã", "â", "A", "Á", "À", "Ã", "Â",
          "e", "é", "ê", "E", "É", "Ê",
          "i", "í", "I", "Í",
          "o", "ó", "ô", "õ", "O", "Ó", "Ô", "Õ",
          "u", "ú", "ü", "U", "Ú", "Ü"]
def inspetor(palavraD):
    quantidade = 0
    for letra in (palavraD):
       if letra in vogais:
           quantidade = quantidade+1
    return(quantidade)
frase = input("digite a frase que será analisada: ")
Qv = inspetor(frase)
print(f"A frase pergutada possui {Qv} vogais")
