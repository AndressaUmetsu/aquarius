#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *

#símbolo, função, limite superior, limite inferior, número de iterações
def bissecao (px, pf, x0, x1, it):
    x = Symbol(px)
    f = sympify(pf)

    for i in range(0, it):
        print ("Iteração", i+1)
        fx0   = f.subs(x, x0)
        fx1   = f.subs(x, x1)
        meio  = x0 + (x1-x0)/2
        fmeio = f.subs(x, meio)
        
        print ("x0   =", x0, "\t f(x0) =", fx0) 
        print ("x1   =", x1, "\t f(x1) =", fx1)
        print ("meio =", meio, "\t f(meio) =", fmeio)
        print
        
        if fmeio * fx0 > 0:
            x0 = meio
        elif fmeio * fx1 > 0:
            x1 = meio
        else:
            break
    print ("Erro estimado:", abs(x0-x1)/2**it)

bissecao ('x', 'ln(x) * cos(x)', 1.1, 2.1, 15)