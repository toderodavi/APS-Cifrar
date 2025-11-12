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

def apagarConteudoArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'w', encoding="utf-8")
    arquivo.close()

def lerConteudoArquivo(nomeArquivo):
    conteudoArquivo = []
    linhas = []
    # Toda seção de try.. except está testando se o arquivo
    # está codificado em utf-8 ou cp1252. O padrão atual é utf-8,
    # mas os arquivos enviados pelo Olavo aparentam estar em cp1252;
    # Basicamente, se o nome do arquivo inserido não for encontrado
    # ou não ser decodificado por utf-8 ou cp1252, será retornada uma lista vazia
    # para que o programa não pare de funcionar (apenas mostre o erro no terminal).
    try:
        arquivo = open(nomeArquivo, "r", encoding="utf-8")
        linhas = arquivo.readlines()
        arquivo.close()
    except UnicodeDecodeError:
        try:
            arquivo = open(nomeArquivo, "r", encoding="cp1252")
            linhas = arquivo.readlines()
            arquivo.close()
        except Exception:
            print(f"Não foi possível ler o arquivo '{nomeArquivo}' como UTF-8 ou cp1252.")
            return []
        
    except FileNotFoundError:
        print(f"Arquivo '{nomeArquivo}' não encontrado.")
        return []
    
    # Itero linha por linha do arquivo, retirando \n do final de uma
    # E faço cada linha virar uma lista com strings usando como separador o ','
    for linha in linhas:
        conteudoArquivo.append(linha.replace('\n', '').split(','))
    return conteudoArquivo

def formatarNomeArquivo(nomeArquivo):
    # Retira sufixos do arquivo (.txt / .csv / Cifrado / Decifrado)
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
    # Recebe os nomes dos arquivos
    print("Para a depuração de votos, insira ao menos dois arquivos.")
    while True:  
        nomesArquivos.append(input("Insira o nome do arquivo:\n").strip())
        if len(nomesArquivos) >= 2:
            escolha = input("Deseja adicionar mais um arquivo?  s/n\n").strip()
            if escolha == 's':
                continue
            else:
                break
    # Acessa arquivo por arquivo, somando os votos
    for i in range(len(nomesArquivos)):
        arquivo = lerConteudoArquivo(nomesArquivos[i])
        # Se meu arquivo for uma lista vazia, pula esta iteração
        if not arquivo:
            continue
        # Se meu csvConstante estiver vazio, receberá a parte constante
        # dos csvs das urnas (as colunas de número e nome dos candidatos)
        if not csvConstante:
            for linha in range(len(arquivo)):
                csvConstante.append(arquivo[linha][:-1])     
                if linha != 0:
                    somaVotos.append(int(arquivo[linha][-1]))     
        else:
            for linha in range(len(arquivo)):
                    if linha != 0:
                        somaVotos[linha-1] += (int(arquivo[linha][-1]))
                        
    if not somaVotos:
        print("Não foi possível realizar a depuração.")
    else:
        # Transforma os votos em strings e as insere novamente ao CSV
        for linha in range(len(somaVotos)):
            somaVotos[linha] = str(somaVotos[linha])
        somaVotos.insert(0, 'Total de Votos')
        for linha in range(len(csvConstante)):
            csvConstante[linha].append(somaVotos[linha])
        gerarArquivo('DepuraçãoVotos', csvConstante)
        print("Depuração realizada.")