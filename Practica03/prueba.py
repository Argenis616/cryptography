import base64
import os
imageread = open("Four.txt",'rb')
decode = imageread.read()
textosinlinea = decode.rstrip('\n')
print(len(decode))
print(len(textosinlinea))
#newimage = open("imagenes.png",'wb')
#newimage.write(decode)