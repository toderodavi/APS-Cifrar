def criarArquivo(fileName):
    open(fileName, "w", encoding="utf-8")

def inserirConteudoArquivo(fileName, content):
    arquivo = open(fileName, "w", encoding="utf-8")
    arquivo.write(content)
    arquivo.close()

def lerConteudoArquivo(file):
    file = open(file, "r", encoding="utf-8")
    conteudoArquivo = file.readlines()
    file.close()
    return conteudoArquivo