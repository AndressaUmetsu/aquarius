#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *

#símbolo, função, valor inicial, número de iterações
def pfixo (px, pf, x0, it):
    x = Symbol(px)
    f = sympify(pf)
    print ("f(x) =", pf, "\n")

    for i in range(0, it):
        print ("Iteração", i+1)
        fx0  =  f.subs(x, x0).evalf()

        print ("x =", x0, "\t", "f(x) =", fx0)
        x0   = fx0

pfixo ('x', 'ln(10/x)', 1, 15)
# pfixo ('x', 'ln(x) * cos(x)', 1.1, 15) #não converge
