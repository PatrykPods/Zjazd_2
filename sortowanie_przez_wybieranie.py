lista = [9,1,6,8,4,3,2,0]
lista_2 = []


for x in lista :
    if x == min(lista) :
        lista_2.append(x)
        del lista[min(lista)]
print(lista)
print(lista_2)

