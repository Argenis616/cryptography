import EllipticCurves
from fractions import gcd
from random import randint
import ECMTests
import math
from sympy import mod_inverse
from EllipticCurves import Curve
from math import gcd as mcd

def coprimo(a, b): return mcd(a, b) == 1

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return False
    else:
        return True

def lenstra(n):
    """
    Implementación del algoritmo de Lenstra para encontrar los factores
    primos de un número n de la forma n = p*q. Se asume que la proposición
    anterior es cierta, es decir, que en efecto n = p*q, regresando ambos
    factores de n.
    """
    x = randint(0, n - 1)
    y = randint(0, n - 1)
    a = randint(0, n - 1)
    b = (y**2 - x**3 - a * x) % n
    curva = Curve(a,b,n)
    p = x
    q = y
    punto = (p,q)
    punto2 = (p,q)
    #respuesta = EllipticCurves.add_points(punto,punto2,curva)
    respuesta = ()
    #hago la primer suma del punto consigomismo
    while True:
        #Tomo un punto sobre la curva y lo sumo con él mismo hasta que no tenga inverso multiplicativo.
        #aqui compruebo que no tengo inversio multiplicativo
        denominador = 0
        if punto == punto2:
            denominador = 2*punto2[1]
        else:
            denominador = punto[0] - punto2[0]
        if modinv(denominador,n) == False:
            factor1 = mcd(denominador,n)
            factor2 = n//factor1
            if factor1 == n or factor1 == 1:
                return lenstra(n)
                break
            else:
                return (int(factor1),int(factor2))
                break
        else:
            punto2 = EllipticCurves.add_points(punto,punto2,curva)
            #respuesta = EllipticCurves.add_points(punto,punto2,curva)
