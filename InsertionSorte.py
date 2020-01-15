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


def insertionsort(lista):
    cont0 = 1
    while cont0 < len(lista):
        cont1 = cont0
        cont2 = cont0
        while cont1 > 0:
            cont1 -= 1
            if lista[cont2] < lista[cont1]:
                aux = lista[cont2]
                lista[cont2] = lista[cont1]
                lista[cont1] = aux
                cont2 -= 1
        cont0 += 1
    return lista


def desenhagrafico(x, y, z, xl = "Entradas", yl = "Saidas"):
    plt.plot(x, y, label="Caso Médio")
    plt.plot(x, z, label="Pior Caso")
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.title("InsertionSort")
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()

xg = [1000, 10000, 30000, 50000, 70000, 100000]
yg = []
zg = []

for i in xg:
    listacm = geralista(i)
    listapc = geralistapc(i)
    val1 = timeit.timeit("insertionsort({})".format(listacm), setup="from __main__ import insertionsort", number=1)
    yg.append(val1)
    val2 = timeit.timeit("insertionsort({})".format(listapc), setup="from __main__ import insertionsort", number=1)
    zg.append(val2)
    print(val1, val2)

desenhagrafico(xg, yg, zg)