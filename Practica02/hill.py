from utils import matriz_text,matriz_llave,matriz_string,valid_key,matriz_llave_inversa
import numpy as np
from numpy import matrix
from numpy.linalg import inv,det
import math

class Hill():

    def __init__(self, alphabet, n, key=None):
        """
        Constructor de clase, recibiendo un alfabeto completamente necesario pero
        podría no recibir una llave de cifrado, en cuyo caso, hay que generar una,
        para el caso del tamañHo de la llave, hay que asegurarse que tiene raíz entera.
        :param alphabet: una cadena con todos los elementos del alfabeto.
        :param n: el tamaño de la llave, obligatorio siempre.
        :param key: una cadena que corresponde a la llave, en caso de ser una llave inválida
        arrojar una CryptographyException.
        """
        self.alphabet=alphabet
        self.n=n
        if key!=None:
            self.key=valid_key(key,self.alphabet,self.n) 
        else:
            self.key=valid_key("BBCD",self.alphabet,self.n) 
        


    def cipher(self, message):
        """
        Aplica el algoritmo de cifrado con respecto al criptosistema de Hill, el cual recordando
        que todas las operaciones son mod |alphabet|.
        :param message: El mensaje a enviar que debe ser cifrado.
        :return: Un criptotexto correspondiente al mensaje, este debe de estar en representación de
        cadena, no lista.
        """
        message=message.replace(" ","")
        while len(message)%int(math.sqrt(self.n))!=0: 
            message+="A"

        matrix_message=matriz_text(message,self.alphabet,self.n)
        k=matriz_llave(self.key,self.alphabet)
        encript=[]
        for  m in matrix_message:
            result=k*m
            f = lambda x: x%len(self.alphabet)
            result=result.applyfunc(f)
            encript.append(result)
        return matriz_string(encript,self.alphabet)

    def decipher(self, ciphered):
        """
        Usando el algoritmo de decifrado, recibiendo una cadena que se asegura que fue cifrada
        previamente con el algoritmo de Hill, obtiene el texto plano correspondiente.
        :param ciphered: El criptotexto de algún mensaje posible.
        :return: El texto plano correspondiente a manera de cadena.
        """
        matrix_message=matriz_text(ciphered,self.alphabet,self.n)
        k=matriz_llave_inversa(self.key,self.alphabet)
        decript=[]
        for  m in matrix_message:
            result=k*m
            f = lambda x: x%len(self.alphabet)
            result=result.applyfunc(f)
            decript.append(result)
        return matriz_string(decript,self.alphabet)
