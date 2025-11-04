def criarArquivo(fileName, content):
    file = open(f'{fileName}.csv', "w", encoding="utf-8")
    inserirConteudoArquivo(file, content)

def inserirConteudoArquivo(file, content):
    linhasFormatadas = []
    hashString = content[-1]
    linhas = content[:-1]
    if isinstance(hashString, str):
        for linha in linhas:
            linhasFormatadas.append(','.join(linha))
        linhasFormatadas.append(hashString)
    else:
        linhas = content
        for linha in linhas:
            linhasFormatadas.append(','.join(linha))
    content = '\n'.join(linhasFormatadas)
    file.write(content)
    file.close()

def lerConteudoArquivo(file):
    linhas = []
    file = open(file, "r", encoding="utf-8")
    conteudoArquivo = file.readlines()
    file.close()
    for i in conteudoArquivo:
        linhas.append(i.replace('\n', '').split(','))
    return linhas
print(lerConteudoArquivo("Urnas(4-1).csv"))