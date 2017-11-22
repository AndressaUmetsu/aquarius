#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *
from math import sin, cos, abs

#símbolos, lista de funções, valores iniciais, erro relativo
def pfixo (px, pf, x0, per):
    symbols(px)
    px = px.split()
    n = len(px)

    for i in range(0, n):
        pf[i] = lambdify(px, S(pf[i]))

    it = 1
    tabela = Matrix()
    while(true):
        xnovo = []
        xerro = []
        for i in range(0, n):
            xnovo.append(N(pf[i](*x0), 7))
            xerro.append(abs(xnovo[i]-x0[i]))

        erro = max(xerro)/abs(max(max(xnovo),min(xnovo),max(x0),min(x0), key=abs))
        tabela = tabela.col_join(Matrix(1, 3, [it, xnovo, erro]))
        if(erro <= per):
            pprint(tabela)
            return tabela
        x0 = xnovo
        it+=1

tabela = pfixo('x1 x2', ['(sin(x1-x2) - x2)/8', '(-cos(x1*x2) + x1)/8'], [0.1,0], 10**-5)
print(latex(tabela))
