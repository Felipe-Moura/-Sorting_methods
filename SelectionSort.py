from random import randint
import matplotlib.pyplot as plt
import timeit


def geralista(tam):
    lista = []
    x = 0
    while x < tam:
        n = randint(1, 10*tam)
        lista.append(n)
        x += 1
    return lista


def geralistapc(tam):
    lista = []
    while tam > 0:
        lista.append(tam)
        tam -= 1
    return lista


def selectionsort(lista):
    for i in range(0, len(lista)):
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        if lista[i] != lista[minimo]:
            aux = lista[i]
            lista[i] = lista[minimo]
            lista[minimo] = aux
    return lista


def desenhagrafico(x, y, z, xl = "Entradas", yl = "Saidas"):
    plt.plot(x, y, label="Caso Médio")
    plt.plot(x, z, label="Pior Caso")
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.title("SelectionSort")
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()

xg = [1000, 10000, 30000, 50000, 70000, 100000]
yg = []
zg = []

for i in xg:
    listacm = geralista(i)
    listapc = geralistapc(i)
    val1 = timeit.timeit("selectionsort({})".format(listacm), setup="from __main__ import selectionsort", number=1)
    yg.append(val1)
    val2 = timeit.timeit("selectionsort({})".format(listapc), setup="from __main__ import selectionsort", number=1)
    zg.append(val2)
    print(val1, val2)

desenhagrafico(xg, yg, zg)