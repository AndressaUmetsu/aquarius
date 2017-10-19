#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *
x = Symbol('x')

#lista de pontos
def lagrange (lista):
    n = len(lista)
    poli = 0
    L = 0
    for a,b in lista:
        L = b
        for c,d in lista:
            if(a != c):
                L *= (x - c)/(a - c)
        print("Li(x) =", L)
        poli += L

    poli = simplify(poli)
    pprint(poli)
    return poli

lista = [(2,3), (3,6), (4,10)]
# lista = [(-1,-1), (0,0), (1,1), (8,2)]
lagrange(lista)
