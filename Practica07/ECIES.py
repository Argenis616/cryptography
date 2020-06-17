import EllipticCurves
import random
import math
from sympy import mod_inverse
class ECIES():
    def __init__(self, curve, A, B, N, s, p):
        self.curve = curve
        self.A = A
        self.B = B
        self.N = N
        self.s = s
        self.p = p

    def encrypt(self, message):
        alphabet=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcde"
        k = random.randrange(1,self.N)
        U = EllipticCurves.scalar_multiplication(self.A,k,self.curve)
        V = EllipticCurves.scalar_multiplication(self.B,k,self.curve)
        puntoC = (U[0],U[1]%2)
        cipher = [(puntoC,((alphabet.index(char)*V[0]) % self.p)) for char in message]
        print(cipher)
        return cipher

    def decrypt(self, criptotext):
        alphabet=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcde"
        plain = ''
        for elem in criptotext:
            x,y = elem
            s = (pow(x[0],3) + self.curve.A*x[0] + self.curve.B)% self.curve.p
            print(s) 
            while True:
                raiz = math.sqrt(s)
                n = int(raiz)
                if (n*n == s):
                    break
                else:
                    s += self.p
            if x[1]==0:
                raiz = raiz * -1
            descompresion = EllipticCurves.scalar_multiplication((x[0],int(raiz)),self.s,self.curve)
            n = ( y * mod_inverse(descompresion[0],self.p)) % self.p
            plain += str(alphabet[n])
        return plain

        
