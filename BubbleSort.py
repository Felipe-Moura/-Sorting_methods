from random import randint
import matplotlib.pyplot as plt
import timeit

def geraLista(tam):
 lista = []
 x=0
 while x<tam:
    n = randint(1, 10*tam)
    lista.append(n)
    x+=1
 return lista

def geraListapc(tam):
 lista = []
 while tam>0:
    lista.append(tam)
    tam-=1
 return lista


def bubleSort(lista):
 troca = True
 while troca:
   cont1 = 0
   cont2 = 1
   troca = False
   while cont2 < len(lista):
     if lista[cont1]>lista[cont2]:
       troca = True
       aux = lista[cont1]
       lista[cont1] = lista[cont2]
       lista[cont2] = aux
     cont1+=1
     cont2+=1
 return lista


def desenhagrafico(x, y, xl = "Entradas", yl = "Saidas"):
    plt.plot(x, y, label = "Melhor Tempo")
    plt.legend()
    plt.title("Bubblesort")
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()

xg = [1000, 10000, 20000, 30000, 40000, 50000]
yg = []

for i in xg:
 lista1 = geraListapc(i)
 val = timeit.timeit("bubleSort({})".format(lista1), setup="from __main__ import bubleSort", number=1)
 yg.append(val)
 print(val)

desenhagrafico(xg, yg)