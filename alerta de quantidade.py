
estoque = {"Caneta": 15, "Caderno": 4, "Borracha": 22,"Lápis": 8}
alerta = []
for item in estoque:
    if estoque.get(item) < 10:
        alerta.append(item)
for alertinhas in alerta:
    print(f"o item {alertinhas} está em estado de alerta")
    