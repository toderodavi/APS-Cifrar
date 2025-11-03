import utils

# Constantes que representam nosso alfabeto e chave a serem usados
alfabeto = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!'(),-.:;?[]{}ÀÁÂÃàáâãÉÊéêÕÔõôÍíÚúÇç" + '"'
chave = '.kàdNF1â)ãKX2jbÉ:D53ch-YiÃIaE4fÊGJCMe;gL0á6Z,H'

# Função que recebe o tamanho do texto a ser cifrado
# e repete a chave até chegar ao tamanho desse texto
def chave_vigenere(tamanho):
    textoChave = (chave * (tamanho // len(chave) + 1 )) [:tamanho]
    return textoChave

def cifrar_vigenere(texto):
    
    chave = chave_vigenere(len(texto))
    resultado = ''

    # Para cada iteração, j é meu caracter a ser cifrado e k é o caracter da chave.
    # Se j e k tiverem presentes no alfabeto,
    # duas variáveis recebem a posição (index) desses caracteres no alfabeto.
    # Assim, o caracter criptografado será a soma dessas posições dentro do alfabeto.
    for i in range(len(texto)):
        j = texto[i]
        k = chave[i]
        if j in alfabeto and k in alfabeto:
            posicaoTexto = alfabeto.index(j)
            posicaoChave = alfabeto.index(k)
            resultado += alfabeto[(posicaoTexto + posicaoChave) % len(alfabeto)]
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
            posicaoTexto = alfabeto.index(j)
            posicaoChave = alfabeto.index(k)
            resultado += alfabeto[(posicaoTexto - posicaoChave) % len(alfabeto)]
        else:
            resultado += j
    return resultado

def hash(fileContent):
    hashIntSequence = 0
    mult = 1019
    mod = 10**18 + 7
    for linha in range(len(fileContent)):
        for celula in fileContent[linha]:
                for char in celula:
                    hashIntSequence = ((hashIntSequence ^ ord(char)) * mult) % mod
    # Formata a sequência de inteiros para uma hex de até 16 caracteres
    # Caso ele não tenha 16 caracteres, preenche com 0s a esquerda
    hashHexSequence = f'{hashIntSequence:016x}'
    return hashHexSequence
