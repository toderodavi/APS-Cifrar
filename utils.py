def criarArquivo(fileName):
    open(fileName, "w", encoding="utf-8")

def inserirConteudoArquivo(fileName, content):
    arquivo = open(fileName, "w", encoding="utf-8")
    arquivo.write(content)
    arquivo.close()

def lerConteudoArquivo(fileName):
    file = open(fileName, "r", encoding="utf-8")
    conteudoArquivo = file.readlines()
    file.close()
    return conteudoArquivo

def cifrar(content, key):
    encryptedContent = ''
    for i in range(len(content)):
        if ord('a') <= ord(content[i]) <= ord('z'):
            start = ord('a')
            encryptedChar = chr(((ord(content[i]) - start) + key) % 26 + start)
            encryptedContent += encryptedChar
        elif ord('A') <= ord(content[i]) <= ord('Z'):
            start = ord('A')
            encryptedChar = chr(((ord(content[i]) - start) + key) % 26 + start)
            encryptedContent += encryptedChar
        elif ord('À') <= ord(content[i]) <= ord('ÿ'):
            start = ord('À')
            encryptedChar = chr(((ord(content[i]) - start) + key) % 63 + start)
            encryptedContent += encryptedChar
        elif ord('[') <= ord(content[i]) <= ord('`'):
            start = ord('[')
            encryptedChar = chr(((ord(content[i]) - start) + key) % 6 + start)
            encryptedContent += encryptedChar
        elif ord(' ') <= ord(content[i]) <= ord('/'):
            start = ord(' ')
            encryptedChar = chr(((ord(content[i]) - start) + key) % 14 + start)
            encryptedContent += encryptedChar
        elif ord('0') <= ord(content[i]) <= ord('9'):
            start = ord('0')
            encryptedChar = chr(((ord(content[i]) - start) + key) % 10 + start)
            encryptedContent += encryptedChar
    return encryptedContent

def decifrar(content, key):
    decryptedContent = ''
    for i in range(len(content)):        
        if ord('a') <= ord(content[i]) <= ord('z'):
            start = ord('a')
            decryptedChar = chr(((ord(content[i]) - start) - key) % 26 + start)
            decryptedContent += decryptedChar
        elif ord('A') <= ord(content[i]) <= ord('Z'):
            start = ord('A')
            decryptedChar = chr(((ord(content[i]) - start) - key) % 26 + start)
            decryptedContent += decryptedChar
        elif ord('À') <= ord(content[i]) <= ord('ÿ'):
            start = ord('À')
            decryptedChar = chr(((ord(content[i]) - start) - key) % 63 + start)
            decryptedContent += decryptedChar
        elif ord('[') <= ord(content[i]) <= ord('`'):
            start = ord('[')
            decryptedChar = chr(((ord(content[i]) - start) - key) % 6 + start)
            decryptedContent += decryptedChar
        elif ord(' ') <= ord(content[i]) <= ord('/'):
            start = ord(' ')
            decryptedChar = chr(((ord(content[i]) - start) - key) % 14 + start)
            decryptedContent += decryptedChar
        elif ord('0') <= ord(content[i]) <= ord('9'):
            start = ord('0')
            decryptedChar = chr(((ord(content[i]) - start) - key) % 10 + start)
            decryptedContent += decryptedChar
    return decryptedContent