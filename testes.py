import utils

# Recebe o nome do arquivo e conteúdo a ser inserido
nomeArquivo = input("Nome do arquivo: ")
conteudoUsuarioArquivo = input("Conteúdo: ")

# Cria o arquivo, insere o conteúdo no arquivo
# e retorna uma lista com o conteúdo do arquivo
utils.criarArquivo(nomeArquivo)
utils.inserirConteudoArquivo(nomeArquivo, conteudoUsuarioArquivo)
conteudoArquivo = utils.lerConteudoArquivo(nomeArquivo)

# conteudoArquivo é uma lista de listas,
# sendo uma lista interna para cada linha (\n) inserida no arquivo.
# Assim, conteudoArquivo[0] se refere à primeira linha do arquivo,
# conteudoArquivo[1] à segunda linha do arquivo e assim por diante.
# conteudoArquivo[0][0] se refere, então, à primeira letra da primeira linha do arquivo.
for i in range(len(conteudoArquivo[0])):
    print(conteudoArquivo[0][i])