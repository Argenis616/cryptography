def cipher(message):
   """"
   Cifra el mensaje recibido como parámetro con el algoritmo de cifrado
   XOR.
   Parámetro:
      message -- el mensaje a cifrar.
   '"""
   messagecrip = "" 
   for elem in message:
      code = ord(elem)^1
      messagecrip += chr(code)
   return messagecrip

def decipher(criptotext):
   """
   Descifra el mensaje recuperando el texto plano siempre y cuando haya
   sido cifrado con XOR.
   Parámetro:
      cryptotext -- el mensaje a descifrar.
   """
   messagedecrip = ""
   for elem in criptotext:
      code = ord(elem)^1
      messagedecrip += chr(code)
   return messagedecrip