def criarArquivo(fileName):
    open(fileName, "w", encoding="utf-8")

def inserirConteudoArquivo(fileName, content):
    arquivo = open(fileName, "w", encoding="utf-8")
    arquivo.write(content)
    arquivo.close()

def lerConteudoArquivo(file):
    linhas = []
    file = open(file, "r", encoding="utf-8")
    conteudoArquivo = file.readlines()
    file.close()
    for i in conteudoArquivo:
        linhas.append(i.replace('\n', '').split(','))
    return linhas
