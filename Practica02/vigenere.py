import random

def completekey(message,key):	
        m=list(message)
        lengkey=len(key)		
        nueva_m= [m[i:i+lengkey] for i in range(0, len(m),lengkey)]	
        fullkey=""		
        for i in nueva_m:
            if len(i)==lengkey:
                fullkey+=key
            else:
                fullkey+=key[0:len(i)]
        return fullkey
class Vigenere():

    def __init__(self, alphabet, password=None):
        #Recomendación, ingeniárselas para no cargar siempre O(n^2) en memoria aunque esto no
        #será evaluado, con n el tamaño del alfabeto.
        """
        Constructor de clase, recibe un parámetro obligatorio correspondiente al alfabeto
        y un parámetro opcional que es la palabra clave, en caso de ser None, entonces
        generar una palabra pseudoaleatoria de al menos tamaño 4.
        :param alphabet: Alfabeto a trabajar con el cifrado.
        :param password: El password que puede ser o no dada por el usuario.
        """
        self.alphabet = alphabet
        if password != None:
            self.password = password
        else:
            lenght = random.randint(4,19)
            i=0
            password= ""
            while i <= lenght:
                password += random.choice(alphabet)
                i += 1
            self.password=password

    def cipher(self, message):
        """
        Usando el algoritmo de cifrado de vigenere, cifrar el mensaje recibido como parámetro,
        usando la tabla descrita en el PDF.
        :param message: El mensaje a cifrar.
        :return: Una cadena de texto con el mensaje cifrado.
        """
        result = ""
        full = ""
        if len(self.password) < len(message):
            full = completekey(message,self.password)
        else:
            full = message
            
        for i in range(len(message)):
            res = (self.alphabet.index(message[i]) + self.alphabet.index(full[i])) % len(self.alphabet)
            result += self.alphabet[res]
            
        return result


    def decipher(self, ciphered):
        """
        Implementación del algoritmo de decifrado, según el criptosistema de vigenere.
        :param ciphered: El criptotexto a decifrar.
        :return: El texto plano correspondiente del parámetro recibido.
        """
        result = ""
        full = ""
        if len(self.password) < len(ciphered):
            full = completekey(ciphered,self.password)
        else:
            full = ciphered

        for i in range(len(ciphered)):
            res = (self.alphabet.index(ciphered[i]) - self.alphabet.index(full[i])) % len(self.alphabet)
            result += self.alphabet[res]
            
        return result
