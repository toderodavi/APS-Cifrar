alfabeto = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!'(),-.:;?[]{}ÀÁÂÃàáâãÉÊéêÕÔõôÍíÚúÇç" + '"'
chave = '.kàdNF1â)ãKX2jbÉ:D53ch-YiÃIaE4fÊGJCMe;gL0á6Z,H'


def chave_vigenere(tamanho):
    texto_chave = (chave * (tamanho // len(chave) + 1 )) [:tamanho]
    return texto_chave

def cifrar_vigenere(texto):
    chave = chave_vigenere(len(texto))
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

def decifrar_vigenere(textoCifrado):
    chave = chave_vigenere(len(textoCifrado))
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