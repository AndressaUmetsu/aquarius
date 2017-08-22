#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *

#símbolo, função, valor inicial, número de iterações
def pfixo (px, pf, x0, it):
    x = Symbol(px)
    f = sympify(pf)

    for i in range(0, it):
        print ("Iteração", i+1)
        fx0  =  f.subs(x, x0).evalf()
        x0   = fx0
        
        print ("x =", x0, "\n") 

pfixo ('x', 'ln(10/x)', 1, 15)