#Dado um dicionário com o nome de 5 alunos e suas respectivas notas (Ex: {"Lucas": 8.5, "Pedro": 7.0...}),
#faça um script que encontre e imprima o nome do aluno que tirou a maior nota e o que tirou a menor nota,
#sem usar funções prontas como max() ou min().

notas = {"lucas": 8.5,"Pedro": 7.0,"matheus" : 8,"jorge":5,"albert": 10}
aluno_maximo = 0
aluno_minimo = 0
nota_minima = notas.get(next(iter(notas)))
nota_maxima = notas.get(next(iter(notas)))
for nota in notas:
    notaR = notas.get(nota)
    if notaR > nota_maxima:
        nota_maxima = notaR
        aluno_maximo = nota
    if notaR < nota_minima:
        nota_minima = notaR
        aluno_minimo = nota
print(f"o aluno com a menor nota foi {aluno_minimo} e o com a maior foi {aluno_maximo}")