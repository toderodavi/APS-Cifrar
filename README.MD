    # A --> B
    # B --> C

    # ASCII
    # 0-9 --> 48-57
    # A-Z --> 65-90
    # a-z --> 97-122

    # Deletar os espaços entre 58-64 e 91-96
    # (caracteres que não vão ser cifrados)
    # ord() para adquirir a posição em unicode
    # chr(posição) retorna o caracter em unicode, sendo 'posição' um número
    # Recebo uma string, itero cada caracter dele, transformo-o em ord(),
    # adiciono a chave ao valor de ord(), faço voltar a ser chr().
