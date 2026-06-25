#Você tem dois estoques de lojas diferentes:
#loja1 = {"caneta": 10, "lapis": 5}  loja2 = {"lapis": 15, "borracha": 8}
#Crie um código que junte os dois dicionários. Se o item existir nos dois (como o "lapis"), as quantidades devem ser somadas.

loja1 = {"caneta": 10, "lapis": 5}
loja2 = {"lapis": 15, "borracha": 8} 
loja3 = {}
for item in loja1:
    q = loja1.get(item)
    loja3.setdefault(item,q)
for item2 in loja2:
    if any(item2 == item for item in loja3) == True:
        nv = (loja3.get(item)) + (loja2.get(item2))
        loja3.update({item : nv})
    else:
        q = loja2.get(item2)
        loja3.setdefault(item2,q)
print(loja3)
