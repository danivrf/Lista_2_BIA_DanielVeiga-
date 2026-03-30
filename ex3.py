def acertar_senha():

    cont = 1

    while cont <= 3:
        senha = input('Digite uma senha para tentar o acesso ao laboratorio do CEIA: ')

        if senha == 'bia2025':
            print('Acesso liberado!')
        else:
            print(f'senha incorreta!! tentativa {cont} de 3')
            cont += 1
    print('Numero de tentativas maximas atingido!')

acertar_senha()