#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *

#símbolo, função, limite superior, limite inferior, número de iterações
def secante (px, pf, x0, x1, it):
    x = Symbol(px)
    f = sympify(pf)
    print ("f(x) =", pf, "\n")

    for i in range(0, it):
        print ("Iteração", i+1)
        fx0 = f.subs(x, x0).evalf()
        fx1 = f.subs(x, x1).evalf()
        
        aux = x1
        x1  = x1 - ((x1-x0)/(fx1-fx0)*fx1).evalf()
        x0  = aux

        print ("x0   =", x0, "\t f(x0) =", fx0)
        print ("x1   =", x1, "\t f(x1) =", fx1)

# secante ('x', 'ln(x) * cos(x)', 1.1, 2.1, 15)
secante ('x', 'x**3 - 5', 1, 2, 15)
