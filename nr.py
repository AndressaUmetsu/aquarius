#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *
import math

#símbolo, função, valor inicial
def nr (px, pf, x0):
    x = Symbol(px)
    f = sympify(pf)
    df = diff(pf)
    print ("f(x) =", pf, "\n")
    i = 0
    fx0  =  f.subs(x, x0).evalf()
    dfx0 = df.subs(x, x0).evalf()
    x1 = x0
    x0   = x0 - fx0/dfx0
    i+=1
    print ("Iteração", i)
    print ("x =", x0, "\t f(x0) =", fx0, '\n')
    while  (100 * (abs(x1-x0) / abs(x0))) > 0.00001:
        fx0  =  f.subs(x, x0).evalf()
        dfx0 = df.subs(x, x0).evalf()
        x1 = x0
        x0   = x0 - fx0/dfx0
        i+=1
        print ("Iteração", i)
        print ("x =", x0, "\t f(x0) =", fx0, '\n')

nr ('x', '1 + x * sin(x)', 5/2)
