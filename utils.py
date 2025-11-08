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

def formatarNomeArquivo(nomeArquivo):
    # Retirar sufixos do arquivo (.txt / .csv / Cifrado / Decifrado)
    # O arquivo será .txt ou .csv e pode ter Cifrado ou Decifrado
    if nomeArquivo.endswith(('.csv', '.txt')):
        nomeArquivo = nomeArquivo[:-4]
    if nomeArquivo.endswith('Cifrado'):
        nomeArquivo = nomeArquivo.replace('Cifrado', '')
    if nomeArquivo.endswith('Decifrado'):
        nomeArquivo = nomeArquivo.replace('Decifrado', '')
    return nomeArquivo

def depurarVotos():
    # Criar variável para guardar os nomes
    nomesArquivos = []
    csvConstante = []
    somaVotos = []
    # Recebe os nomes dos arquivos antes de acessar cada um
    while True:
        nomesArquivos.append(input("Insira o nome/caminho do arquivo:  "))
        if len(nomesArquivos) >= 2:
            escolha = input("Deseja adicionar mais um arquivo?  s/n  ")
            if escolha == 's':
                continue
            else:
                break
    # Acessa arquivo por arquivo, guardando os dados constantes
    # e somando os votos
    for i in range(len(nomesArquivos)):
        arquivo = lerConteudoArquivo(nomesArquivos[i])
        if i == 0:
            for colunas in range(len(arquivo)):
                if colunas == 0:
                    csvConstante.append(arquivo[colunas][:-1])     
                else:
                    csvConstante.append(arquivo[colunas][:-1])
                    somaVotos.append(int(arquivo[colunas][-1]))     
        else:
            for colunas in range(len(arquivo)):
                    if colunas != 0:
                        somaVotos[colunas-1] += (int(arquivo[colunas][-1]))
    # Transforma os votos em strings e as insere novamente ao CSV
    for linha in range(len(somaVotos)):
        somaVotos[linha] = str(somaVotos[linha])
    somaVotos.insert(0, 'Total de Votos')
    for linha in range(len(csvConstante)):
        csvConstante[linha].append(somaVotos[linha])
    gerarArquivo('DepuraçãoVotos', csvConstante)