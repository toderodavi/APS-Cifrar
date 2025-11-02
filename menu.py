import utils, crypt

questao= input("Deseja utilizar o programa? (s/n) ")
while questao=="s":

    oqfazer=input("\nO que deseja fazer?\n\n1- Criptografar arquivo\n2- Descriptografar arquivo\n\nDigite o número da opção desejada: ")

    if oqfazer not in ["1","2"]:
        oqfazer=input("Opção inválida. Digite o número da opção desejada: ")
    else:
        if oqfazer == "1":
        
    
    # Criptografia de arquivos
    
        
            criptografar=input("\nDeseja criptografar um arquivo? (s/n) ")
            if criptografar == "s":

        #criar o arquivo
                fileName = input("Digite um nome para criar o arquivo que será criptografado: ")
                utils.criarArquivo(fileName)
        #adicionar conteudo ao arquivo
                num_linhas = int(input("Quantas linhas deseja inserir no arquivo? "))
                if num_linhas <= 0:
                    num_linhas = int(input("Essa quantidade não é válida. Insira um outro número: "))
                for i in range(num_linhas):
                    linha = input(f"Digite o conteúdo da linha {i+1}: ")
                    if i == 0:
                        conteudo_atual = linha + "\n"
                    else:
                        conteudo_atual += linha + "\n"
                        i+=1
                utils.inserirConteudoArquivo(fileName, conteudo_atual)
        #criptografar o arquivo
                conteudo = utils.lerConteudoArquivo(fileName)
                texto = ""
                for linha in conteudo:
                    texto += linha
                textoCifrado = crypt.cifrar_vigenere(texto)
                utils.inserirConteudoArquivo(fileName, textoCifrado)
                print("Arquivo criptografado com sucesso!")
                criptografar=input("Deseja criptografar outro arquivo? (s/n) ")


    # Descriptografar arquivos

        elif oqfazer == "2":

            descriptografar=input("\nDeseja descriptografar um arquivo? (s/n) ")
            if descriptografar == "s":
                senha="batata"
               

                fileName = input("Digite o nome do arquivo: ")
                tentativa=input("Digite a senha para descriptografar o arquivo: ")
                if tentativa != senha:
            #mostra o arquivo sem descriptografar
                    conteudo = utils.lerConteudoArquivo(fileName)
                    print("Conteúdo do arquivo:")
                    for linha in conteudo:
                        print(linha.rstrip())

                else:
                    if tentativa == senha:
            #descriptografa o arquivo
                        conteudo = utils.lerConteudoArquivo(fileName)
                        textoCifrado = ""
                        for linha in conteudo:
                            textoCifrado += linha
                        textoDecifrado = crypt.decifrar_vigenere(textoCifrado)
                        fileName = fileName + "descriptografada"
                        utils.criarArquivo(fileName)
                        utils.inserirConteudoArquivo(fileName, textoDecifrado)
            #mostra o arquivo descriptografado
                        conteudo = utils.lerConteudoArquivo(fileName)
                        print("Conteúdo do arquivo:")
                        for linha in conteudo:
                            print(linha.rstrip())
                        print("Arquivo descriptografado com sucesso!")
                        descriptografar=input("Deseja descriptografar outro arquivo? (s/n) ")



print("\n\nPrograma encerrado.")