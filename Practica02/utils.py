import random 
from sympy import Matrix
from numpy.linalg import inv,det
import numpy as np
import math
class CryptographyException(Exception):

    def __init__(self):
        self.message = "Invalid key"

    def __str__(self):
        return self.message

def valid_key(key,alphabet,n):
    leng=int(math.sqrt(n))
    matri =[]
    for i in key:
        matri.append(alphabet.index(i))

    matri2 =[]
    for i in range(0,len(matri),leng):
        matri2.append(matri[i:i+leng])
    matri = Matrix(matri2)
    if (len(key)!=n or leng <(math.sqrt(n))):
        raise CryptographyException
    else:
        determinat = matri.det()
        determinat2 = inv(determinat,len(alphabet))
        if (determinat==0 or determinat2==0):
            raise CryptographyException
        return key

def inv(a,m):
    for b in range(m):
        x=(a*b)%m
        if (x==1):
            return b
    return 0


def matriz_llave(key,alphabet):
    matri =[]
    for i in key:
        matri.append(alphabet.index(i))
    matri2 =[]
    leng=int(math.sqrt(len(key)))
    for i in range(0,len(matri),leng):
        matri2.append(matri[i:i+leng])
    return Matrix(matri2)

def matriz_text(msg,alphabet,n):
    matri =[]
    for i in msg:
        matri.append(alphabet.index(i))
    b=[]
    for j,v in enumerate(matri):
        a=[]
        a.append(v)
        b.append(a)
    
    leng=int(math.sqrt(n))
    matri2 =[]
    for i in range(0, len(b),leng):
        matri2.append(b[i:i+leng])
    matriz_list=[]
    for a in matri2:
        matriz_list.append(Matrix(a))
    return matriz_list

def matriz_llave_inversa(key,alphabet):
    matriz=matriz_llave(key,alphabet)
    k=matriz.adjugate()
    f = lambda x: x%len(alphabet)
    k=k.applyfunc(f)
    determinante=inv(matriz.det(),len(alphabet))
    k= k*determinante
    k=k.applyfunc(f)
    return k

def matriz_string(lst,alphabet):
    txt=[]
    f = lambda x: txt.append(alphabet[x])
    for m in lst:
        m.applyfunc(f)
    s = ''.join(txt)
    return s
