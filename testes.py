import utils, crypt
texto = input("Texto: ")
chave = input("Chave: ")

textoCifrado = crypt.cifrar_vigenere(texto, chave)
print(textoCifrado)
print(crypt.decifrar_vigenere(textoCifrado, chave))