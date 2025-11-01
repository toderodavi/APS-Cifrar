alfabeto = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!'(),-.:;?[]{}ÀÁÂÃàáâãÉÊéêÕÔõôÍíÚúÇç" + '"'

def mensagem_vigenere(mensagem): 
    mensagem = mensagem
    return mensagem

def chave_vigenere(chave, tamanho):
    chave = chave
    texto_chave = (chave * (tamanho // len(chave) + 1 )) [:tamanho]
    return texto_chave

def cifra_vigenere(mensagem, chave):
    # Texto em caixa alta
    texto = mensagem_vigenere(mensagem)
    # Chave da cifra
    chave = chave_vigenere(chave, len(texto))
    resultado = ''

    for i in range(len(texto)):
        j = texto[i]
        k = chave[i]
        if j in alfabeto and k in alfabeto:
            posTexto = alfabeto.index(j)
            posChave = alfabeto.index(k)
            print(j, k, alfabeto[posTexto + posChave])
            resultado += alfabeto[(posTexto + posChave) % len(alfabeto)]
        else:
            resultado += j
    return resultado