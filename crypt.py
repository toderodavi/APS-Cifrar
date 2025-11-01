alfabeto = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!'(),-.:;?[]{}ÀÁÂÃàáâãÉÊéêÕÔõôÍíÚúÇç" + '"'

def chave_vigenere(chave, tamanho):
    texto_chave = (chave * (tamanho // len(chave) + 1 )) [:tamanho]
    return texto_chave

def cifrar_vigenere(texto, chave):
    chave = chave_vigenere(chave, len(texto))
    resultado = ''

    for i in range(len(texto)):
        j = texto[i]
        k = chave[i]
        if j in alfabeto and k in alfabeto:
            posTexto = alfabeto.index(j)
            posChave = alfabeto.index(k)
            resultado += alfabeto[(posTexto + posChave) % len(alfabeto)]
        else:
            resultado += j
    return resultado

def decifrar_vigenere(textoCifrado, chave):
    chave = chave_vigenere(chave, len(textoCifrado))
    resultado = ''

    for i in range(len(textoCifrado)):
        j = textoCifrado[i]
        k = chave[i]
        if j in alfabeto and k in alfabeto:
            posTexto = alfabeto.index(j)
            posChave = alfabeto.index(k)
            resultado += alfabeto[(posTexto - posChave) % len(alfabeto)]
        else:
            resultado += j
    return resultado