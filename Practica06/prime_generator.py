from random import randint
from random import randrange
import random
import math
import sys

def big_int(size=None):
    """
    Generador de números aleatorios de un tamaño fijo recibido como parámetro, si el parámetro es
    menor que 100 o None, entonces la función no le hace caso y genera uno de tamaño arbitrario,
    máximo es de 150 dígitos.
    :return: Un número del tamaño descrito.
    """
    if (size == None) or (size < 100):
        numeroGrande = 10**randint(99,149)
        posiblePrimo = randint(numeroGrande, 2*numeroGrande)
        return posiblePrimo
    else:
        numeroGrande = 10**(size-1)
        posiblePrimo = randint(numeroGrande, 2*numeroGrande)
        return posiblePrimo

def miller_rabin(n):
    """
    Implementación del test de primalidad de Miller-Rabin.
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    def aux_func(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  

    for i in range(8):
        a = random.randrange(2, n)
        if aux_func(a):
            return False
 
    return True 


def wilson(n):
    """
    Implementaión del test de primalidad de Wilson, basado en el teorema de Wilson,
    (p-1)! ≡ -1 mod p
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    return ((factorial(n-1) + 1) % n) == 0

def factorial(n):
    resultado = 1
 
    for i in range(n):
        resultado *= (i + 1)
 
    return resultado
def generate_prime_candidate(length):
    """ Genera un integer impar aleatorimanete 
        param size: tamanio del numero deseado
        return:integer
    """
    p = big_int(length)
    p |= (1 << length - 1) | 1
    return p

def generate_prime(size=None):
    """
    Genera un primo de al menos $size dígitos, si no se especifica,
    este tiene que asegurar que al menos tiene 100 dígitos.

    :param size: El tamaño del primo a generar.
    :return: Un número que se asegura que es primo.
    """
    if size == None:
        primo = big_int(100)
        while not miller_rabin(primo):
            primo = generate_prime_candidate(100)
        return primo
    else:
        primo = big_int(size)
        while not miller_rabin(primo):
            primo = generate_prime_candidate(size)
        return primo

