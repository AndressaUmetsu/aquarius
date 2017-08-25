#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *

#símbolo, função, valor inicial, número de iterações
def nr (px, pf, x0, it):
    x = Symbol(px)
    f = sympify(pf)
    df = diff(pf)
    print ("f(x) =", pf, "\n")

    for i in range(0, it):
        print ("Iteração", i+1)
        fx0  =  f.subs(x, x0).evalf()
        dfx0 = df.subs(x, x0).evalf()
        x0   = x0 - fx0/dfx0

        print ("x =", x0, "\t f(x0) =", fx0, '\n')

nr ('x', 'ln(x) * cos(x)', 2.0, 15)
