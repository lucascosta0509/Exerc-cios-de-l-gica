# peça para o usuário digitar um valor de saque inteiro (Ex: R$ 130). O programa deve dizer quantas notas de R$ 50, R$ 20 e R$ 10
# serão entregues. (Tente entregar o menor número de cédulas possível).

def notas(valorE):
    qn = {}
    Q50 = (valorE/50) - (valorE/50 %1)
    qn.setdefault("q50",Q50)
    resto = valorE - (Q50*50)
    Q20 = (resto/20) - (resto/20 %1)
    qn.setdefault("q20",Q20)
    resto = resto - (Q20*20)
    Q10 = (resto/10) - (resto/10 %1)
    qn.setdefault("q10",Q10)
    resto = valorE - ((Q50*50)+(Q20*20)+(Q10*10))
    qn.setdefault("resto",resto)
    return qn
SI = int(input("digite o valor a ser sacado(está maquina disponibiliza apenas notas de 10, 20 e 50): "))
dados = notas(SI)
print(f"foram necessarias {dados.get("q50")} notas de 50, {dados.get("q20")} notas de 20, {dados.get("q10")} notas de 10 e {dados.get("resto")} reais não foram possiveis de serem sacados")
