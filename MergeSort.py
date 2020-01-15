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
    x = 0
    while x < tam:
        lista.append(tam)
        tam -= 1
    return lista


def mergesort(lista):
    if len(lista) > 1:
        pivo = int(len(lista)/2)
        esq = []
        dir = []
        i = 0
        while i < len(lista):
            if i < pivo:
                esq.append(lista[i])
            else:
                dir.append(lista[i])
            i += 1
        mergesort(esq)
        mergesort(dir)
        j = 0
        k = 0
        l = 0
        while j < len(esq) and k < len(dir):
            if esq[j] < dir[k]:
                lista[l] = esq[j]
                j += 1
            else:
                lista[l] = dir[k]
                k += 1
            l += 1
        while j < len(esq):
            lista[l] = esq[j]
            j += 1
            l += 1
        while k < len(dir):
            lista[l] = dir[k]
            k += 1
            l += 1
    return lista


def desenhagrafico(x, y, z, xl = "Tamanho da lista", yl = "Tempo"):
    plt.plot(x, y, label="Caso Médio")
    plt.plot(x, z, label="Pior Caso")
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.title("MergeSort")
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()

xg = [1000, 5000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
yg = []
zg = []

for i in xg:
    listacm = geralista(i)
    listapc = geralistapc(i)
    val1 = timeit.timeit("mergesort({})".format(listacm), setup="from __main__ import mergesort", number=1)
    yg.append(val1)
    val2 = timeit.timeit("mergesort({})".format(listapc), setup="from __main__ import mergesort", number=1)
    zg.append(val2)
    print(val1, val2)

desenhagrafico(xg, yg, zg)