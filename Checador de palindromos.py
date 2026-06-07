print("ANALISADOR DE PALINDROMOS")
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
        if junto == (palavraN):
            resultado = True
        else:
            resultado = False
        return resultado
        
    palavra = str(input("escreva a palavra a ser analisada(caso seja mais de uma palavra escreva junto:): "))
    resultadoR = invertedor(palavra)
    if resultadoR ==True:
        print(f"a palavra {palavra} é um palindromo")
    else:
        print(f"a palavra {palavra} não é um palindromo")