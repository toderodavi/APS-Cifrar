import utils

text = input("Texto: ")
key = int(input("Chave: "))

encryptedText = utils.cifrar(text, key)
print(encryptedText)
print(utils.decifrar(encryptedText, key))