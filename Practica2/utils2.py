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

def creaLlave(alphabet,n,longitud):
	semilla=[]
	for i in range(len(alphabet)):
		if (impr(i,len(alphabet))!=0):
			semilla.append(i)
	llave=[]
	for i in range(n):
		aleatorio=random.choice(semilla)
		llave.append(aleatorio)

	valid=True
	while valid:
		text=[alphabet[x] for x in list(llave)]
		text=''.join(text)
		try:
			validaLLave(text,longitud,alphabet,n)
			valid=False
		except:
			llave.remove(random.choice(llave))
			aleatorio=random.choice(semilla)
			llave.append(aleatorio)
	return text
	
def validaLLave(key,longitud,alphabet,n):
	m=[alphabet.index(x) for x in list(key)]
	nueva_m= [m[i:i+longitud] for i in range(0, len(m),longitud)]
	m=Matrix(nueva_m)
	if (len(key)!=n or longitud<(math.sqrt(n))):
		raise CryptographyException
	else:
		det=m.det()
		idet=impr(det,len(alphabet))
		if (det==0 or idet==0):
			raise CryptographyException

def creaMatrizLlave(key,longitud,alphabet):

	a=[alphabet.index(x) for x in list(key)]
	b= [a[i:i+longitud] for i in range(0, len(a),longitud)]	
	return Matrix(b)

def creaMatriz(m,longitud,alphabet):

	m=[alphabet.index(x) for x in list(m)]
	b=[]
	for j,v in enumerate(m):
		a=[]
		a.append(v)
		b.append(a)
	nueva_2= [b[i:i+longitud] for i in range(0, len(b),longitud)]
	matriz_list=[]
	for a in nueva_2:
		matriz_list.append(Matrix(a))
	return matriz_list

def matrizToString(lst,alphabet):

	txt=[]
	f = lambda x: txt.append(alphabet[x])
	for m in lst:
		m.applyfunc(f)
	s = ''.join(txt)
	return s

def inversamodular(matriz_llave,len_alphabeto):

	k=matriz_llave.adjugate()
	f = lambda x: x%len_alphabeto
	k=k.applyfunc(f)
	determinante=impr(matriz_llave.det(),len_alphabeto)
	k= k*determinante
	k=k.applyfunc(f)
	return k

def impr(a,m):

	for b in range(m):
	    x=(a*b)%m
	    if (x==1):
	        return b
	return 0

def div(texto,llave):
	m=list(texto)
	longkey=len(llave)		
	nueva_m= [m[i:i+longkey] for i in range(0, len(m),longkey)]	
	llavecompleta=""		
	for i in nueva_m:
		if len(i)==longkey:
			llavecompleta+=llave
		else:
			llavecompleta+=llave[0:len(i)]
	return llavecompleta

def creaLlaveV(alphabet,len_message):

	n=len_message if (4>len_message) else random.randint(4,len_message)
	lista_par=[]
	lista_impar=[]
	for i in range(len(alphabet)):
		if(i%2==0):
			lista_par.append(alphabet[i])
		else:
			lista_impar.append(alphabet[i])
	
	llave=""
	for i in range(n):
		if(i%2==0):
			a=random.randint(0,len(lista_par)-1)
			llave=llave+lista_par[a]
		else:
			a=random.randint(0,len(lista_impar)-1)
			llave=llave+lista_impar[a]
	return llave

