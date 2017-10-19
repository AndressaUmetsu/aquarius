#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *
x = Symbol('x')

#lista de pontos
def newton (lista):
    n = len(lista)
    matriz = zeros(n,n+1)
    i = 0
    for a, b in lista:
        matriz[i, 0] = a
        matriz[i, 1] = b
        i += 1
    for j in range(2, n+1):
        for i in range(0, n-j+1):
            matriz[i,j] = (matriz[i+1,j-1] - matriz[i,j-1]) / (matriz[i+j-1, 0] - matriz[i, 0])

    print(matriz)

    poli = 0
    aux  = 1
    for j in range(1, n+1):
        if(j>1):
            aux *= (x - matriz[j-2, 0])
        poli += matriz[0,j]*aux
    poli = simplify(poli)
    pprint (poli)
    return poli

# lista = [(2,3), (3,6), (4,10)]
lista = [(-1,-1), (0,0), (1,1), (8,2)]
poli = newton(lista)
# print(poli.subs(x,2))
