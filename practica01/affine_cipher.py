from math import gcd as mcd
from utils import CryptographyException
def coprimo(a, b): return mcd(a, b) == 1

def inv(a,m):
    for elem in range(m):
        x=(a * elem)%m
        if (x==1):
            return elem
    return 0
class Affine():

    def __init__(self, alphabet, A=None, B=None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado afín.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            A -- El coeficiente A que necesita el cifrado.
            B -- El coeficiente B de desplazamiento.
        """
        self.alphabet = alphabet
        A= A if A else 1
        if coprimo(A,len(alphabet)):
            self.A = A
        else:
            raise CryptographyException
        self.B=B if B else 0

    def cipher(self, message):
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado afín, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        cifrad=""
        for elem in message:
            cifrad += self.alphabet[(self.A * self.alphabet.index(elem) + self.B) % len(self.alphabet)]
        return cifrad

    def decipher(self, criptotext):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el cifrado afín.
        Parámetro:
            criptotext -- el mensaje a descifrar.
        """
        inverso=inv(self.A,len(self.alphabet))
        cifrad=""
        for elem in criptotext:
            cifrad += self.alphabet[(inverso*(self.alphabet.index(elem)-self.B)) % len(self.alphabet)]
        return cifrad

    