import utils, crypt

while True:
    oqfazer=input("\nO que deseja fazer?\n\n1- Criptografar arquivo\n2- Descriptografar arquivo\n3- Depurar votos\n4- Sair\n\nDigite o número da opção desejada: ")
    if oqfazer not in ["1","2", "3", "4"]:
        oqfazer=input("Opção inválida. Digite o número da opção desejada: ")
    else:
        # Criptografar arquivos
        if oqfazer == "1":
            while True:
                nomeArquivo = input("Insira o nome do arquivo que deseja criptografar: ")
                crypt.CifrarCSV(nomeArquivo)
                print("Arquivo criptografado com sucesso!")
                oqfazer=input("Deseja criptografar outro arquivo? (s/n) ")
                if oqfazer != 's':
                    break

        # Descriptografar arquivos
        elif oqfazer == "2":
            while True:
                nomeArquivo = input("Insira o nome do arquivo que deseja descriptografar: ")
                crypt.DecifrarCSV(nomeArquivo)
                oqfazer=input("Deseja criptografar outro arquivo? (s/n) ")
                if oqfazer != 's':
                    break

        # Depuração de votos
        elif oqfazer == "3":
            utils.depurarVotos()

        elif oqfazer == "4":
            break

print("\n\nPrograma encerrado.")