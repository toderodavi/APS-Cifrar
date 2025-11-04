import utils, crypt

# Variáveis 
file = 'text.txt'
linhasCriptografadas = []
linhasDescriptografadas = []
celulaCriptografada = []
celulaDescriptografada = []
linhasParaDescriptografar = []
primeiroHash = ''
segundoHash = ''
linhasArquivo = utils.lerConteudoArquivo(file)

# Encriptar o .csv
for linha in range(len(linhasArquivo)):
    for celula in linhasArquivo[linha]:
        celulaCriptografada.append(crypt.cifrar_vigenere(celula))
    linhasCriptografadas.append(celulaCriptografada)
    celulaCriptografada = []
linhasCriptografadas.append(crypt.hash(linhasArquivo))
print(linhasCriptografadas)
utils.criarArquivo("umCsvDeTeste", linhasCriptografadas)

linhasParaDescriptografar = utils.lerConteudoArquivo("umCsvDeTeste.csv")
primeiroHash = linhasCriptografadas[-1]
linhasParaDescriptografar = linhasCriptografadas[:-1]

# Descriptar o .csv
for linha in range(len(linhasParaDescriptografar)):
    for celula in linhasParaDescriptografar[linha]:
            celulaDescriptografada.append(crypt.decifrar_vigenere(celula))
    linhasDescriptografadas.append(celulaDescriptografada)
    celulaDescriptografada = []
print(linhasDescriptografadas)
segundoHash = crypt.hash(linhasDescriptografadas)
if primeiroHash == segundoHash:
     print("Conteúdo original mantido!")
     utils.criarArquivo("umCsvDeTesteDescriptografado", linhasDescriptografadas)
else:
     print("Conteúdo original comprometido!!!!")
     utils.inserirConteudoArquivo("UmCsvDeTeste", '')