from prime_generator import generate_prime
import random
import math
import sys
from math import gcd as mcd
from sympy import mod_inverse
def coprimo(a, b): return mcd(a, b) == 1


class RSA():

    def __init__(self):
        """
        Constructor de RSA, aquí se deben de generar los primos p y q
        para que puedan ser vistos por toda la clase, así como la llave
        pública y privada.
        """
        self.padding_scheme = False
        self.p = generate_prime()
        self.q = generate_prime()
        self.n = self.p * self.q
        self.phi = (self.p - 1)*(self.q - 1)
        self.e = random.randrange(1, self.phi)
        self.g = coprimo(self.e,self.phi)
        while self.g != 1:
            self.e = random.randrange(1, self.phi)
            self.g = coprimo(self.e, self.phi)
        self.d = mod_inverse(self.e,self.phi)
        self.priv_key = self.d
        self.pub_key = self.e
        #Aquí también deben de generar su priv_key y pub_key
        f_public = open('public_keys.txt', 'w')
        f_public.write(str(self.n) + '\n')
        f_public.write(str(self.e) + '\n')
        f_public.close()

        f_private = open('private_keys.txt', 'w')
        f_private.write(str(self.n) + '\n')
        f_private.write(str(self.d) + '\n')
        f_private.close()

    def __phi__(self):
        """
        Función completamente privada y auxiliar, únicamente para el uso de las
        pruebas unitarias.
        :return: el número de primos relativos con n.
        """
        return self.phi

    def encrypt(self, message):
        """
        Encripta un mensaje recibido como parámetro y lo regresa a manera
        de lista de enteros.
        :param message: el mensaje a encriptar.
        :return: una lista de enteros con el mensaje encriptado.
        """
        cipher = [pow(ord(char),self.e,self.n) for char in message]
        return cipher

    def decrypt(self, criptotext):
        """
        Desencripta un criptotexto cifrado con RSA y lo regresa a manera
        de cadena, recuperando la información del mensaje original.
        :param criptotext: el mensaje recibido que se va a desencriptar.
        :return: una cadena con el mensaje original.
        """
        plain = [chr(pow(char, self.d,self.n)) for char in criptotext]
        return ''.join(plain)
        
