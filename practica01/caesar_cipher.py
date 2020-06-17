class Caesar():

    def __init__(self, alphabet, key=None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado de César.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            key -- el tamaño del desplazamiento sobre el alfabeto, si es
                   None, se debe de escoger una llave aleatoria, válida.
        """
        self.alphabet = alphabet
        self.key = key if key else 1

    def cipher(self, message, flag=None):
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado césar, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        if flag == True:
            cifrad=""
            for elem in message:
                if elem==" ":
                    cifrad += " "
                else:
                    cifrad += str(self.alphabet[(self.alphabet.index(elem)+self.key)%(len(self.alphabet))])
            return cifrad
        else:

            cifrad=""
            ban=True
            try:
                self.alphabet.index(" ")
            except:
                ban=False
            for elem in message:
                if (elem==" " and not ban):
                    pass
                else:
                    cifrad += str(self.alphabet[(self.alphabet.index(elem)+self.key)%(len(self.alphabet))])
            return cifrad

    def decipher(self, criptotext, flag=None):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el algoritmo de césar.
        Parámetro:
            cryptotext -- el mensaje a descifrar.
        """
        if flag == True:
            cifrad=""
            for elem in criptotext:
                if elem==" ":
                    cifrad += " "
                else:
                    cifrad += str(self.alphabet[(self.alphabet.index(elem)-self.key)%(len(self.alphabet))])
            return cifrad
        else:
            cifrad=""
            for elem in criptotext:
                cifrad += str(self.alphabet[(self.alphabet.index(elem)-self.key)%(len(self.alphabet))])
            return cifrad