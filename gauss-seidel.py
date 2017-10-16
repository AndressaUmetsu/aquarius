#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *
x = Symbol('x')

#matriz A, vetor B, número de iterações 
def gseidel (A, B, it):
    n = len(B)
    A = Matrix(A)
    B = Matrix(B)
    M = zeros(n,1)

    for k in range(1, it+1):
        for i in range(0, n):
            M[i] = B[i]
            for j in range(0, n):
                if(j!=i):
                    M[i] -= M[j]*A[i,j]
            M[i] /= A[i,i]
        print("\nIteração", k)
        pprint(M.evalf())
    return M

M = gseidel([[4,3], [-2,5]], [5,4], 3)
