#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *

#símbolo, função, limite superior, limite inferior, número de iterações
def bissecao (px, pf, x0, x1):
    x = Symbol(px)
    f = sympify(pf)
    i = 0

    print ("f(x) =", pf, "\n")
    
    erroP = abs(x0 - x1)/abs(x1)
    while erroP > 0.00001:
        i+=1
        print ("\nIteração ", i)

        fx0   = f.subs(x, x0).evalf()
        fx1   = f.subs(x, x1).evalf()
        meio  = x0 + (x1-x0)/2
        fmeio = f.subs(x, meio).evalf()
        erroP = (abs(x0 - x1)/abs(x1))*100

        print ("erro =", erroP, '\n')
        print ("x0   =", x0, "\t f(x0) =", fx0)
        print ("x1   =", x1, "\t f(x1) =", fx1)
        print ("meio =", meio, "\t f(meio) =", fmeio, '\n')
        
        if fmeio * fx0 > 0:
            x0 = meio
        elif fmeio * fx1 > 0:
            x1 = meio
        else:
            break
    # print ("Erro estimado :", abs(x0-x1)/2**it)

bissecao ('x', '1 + x*sin(x)', 0, 3*pi.evalf()/2)