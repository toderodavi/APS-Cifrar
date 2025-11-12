import utils, crypt

while True:
    oqfazer=input("\nO que deseja fazer?\n\n1- Criptografar arquivo\n2- Descriptografar arquivo\n3- Depurar votos\n4- Sair\n\nDigite o número da opção desejada: ").strip()
    while oqfazer not in ["1","2", "3", "4"]:
        oqfazer=input("Opção inválida. Digite o número da opção desejada: ").strip()
        # Criptografar arquivos
    if oqfazer == "1":
        while True:
            nomeArquivo = input("\nInsira o nome do arquivo que deseja criptografar: ").strip()
            crypt.CifrarCSV(nomeArquivo)
            oqfazer=input("Deseja criptografar outro arquivo? (s/n) ").strip()
            if oqfazer != 's':
                break

        # Descriptografar arquivos
    elif oqfazer == "2":
        while True:
            nomeArquivo = input("\nInsira o nome do arquivo que deseja descriptografar: ").strip()
            crypt.DecifrarCSV(nomeArquivo)
            oqfazer=input("Deseja descriptografar outro arquivo? (s/n) ").strip()
            if oqfazer != 's':
                break

    # Depuração de votos
    elif oqfazer == "3":
        utils.depurarVotos()

    # Sair do programa
    elif oqfazer == "4":
        break

print("\nPrograma encerrado.")