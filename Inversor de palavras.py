func = True
while func == True:
    def invertedor(palavraN):
        palavraP = list(palavraN)
        tamanho = len(palavraP)
        palavraI = []
        for i in range(0, tamanho):
            novaL = palavraP[tamanho-1]
            tamanho = tamanho - 1
            palavraI.append(novaL)
        junto = "".join(palavraI)
        return junto
        
    palavra = str(input("escreva a palavra que será invertida: "))
    palavraR = invertedor(palavra)
    print(f"Sua palavra invertida é {palavraR}")

    