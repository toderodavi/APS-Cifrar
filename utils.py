def gerarArquivo(nomeArquivo, conteudo):
    arquivo = open(f'{nomeArquivo}.csv', "w", encoding="utf-8")
    linhasFormatadas = []
    
    # Checa se tenho ou não um hash
    # Se tiver, guardo ele. Se não, defino como None
    if isinstance(conteudo[-1], str):
        hashString = conteudo[-1]
        linhas = conteudo[:-1]
    else:
        hashString = None
        linhas = conteudo
    
    # Reformata os valores de dentro das listas
    # para que sejam separadas por vírgula
    for linha in linhas:
        linhasFormatadas.append(','.join(linha))

    # Caso eu tenha um hash, adiciona ao final do documento
    if hashString is not None:
        linhasFormatadas.append(hashString)

    linhasFormatadas = '\n'.join(linhasFormatadas)
    arquivo.write(linhasFormatadas)
    arquivo.close()

def excluirArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'w', encoding="utf-8")
    arquivo.close()

def lerConteudoArquivo(nomeArquivo):
    conteudoArquivo = []
    arquivo = open(nomeArquivo, "r", encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()
    # Itero linha por linha do arquivo, retirando \n do final de uma
    # E faço cada linha virar uma lista com strings usando como separador o ','
    for linha in linhas:
        conteudoArquivo.append(linha.replace('\n', '').split(','))
    return conteudoArquivo