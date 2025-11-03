import utils, crypt
file = 'text.txt'
linhasCriptografadas = []
linhasDescriptografadas = []
celulaCriptografada = []
celulaDescriptografada = []
linhasParaDescriptografar = []
primeiroHash = ''
segundoHash = ''
linhasArquivo = utils.lerConteudoArquivo(file)

for linha in range(len(linhasArquivo)):
    for celula in linhasArquivo[linha]:
        celulaCriptografada.append(crypt.cifrar_vigenere(celula))
    linhasCriptografadas.append(celulaCriptografada)
    celulaCriptografada = []
linhasCriptografadas.append(crypt.hash(linhasArquivo))
print(linhasCriptografadas)

primeiroHash = linhasCriptografadas[-1]
linhasParaDescriptografar = linhasCriptografadas[:-1]

for linha in range(len(linhasParaDescriptografar)):
    for celula in linhasParaDescriptografar[linha]:
            celulaDescriptografada.append(crypt.decifrar_vigenere(celula))
    linhasDescriptografadas.append(celulaDescriptografada)
    celulaDescriptografada = []
print(linhasDescriptografadas)
segundoHash = crypt.hash(linhasDescriptografadas) 
if primeiroHash == segundoHash:
     print("Conteúdo original mantido!")
else:
     print("Conteúdo original comprometido!!!!")
