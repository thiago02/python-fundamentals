menu = '''     -= Sistema =-
     1) Cadastrar usuario
     2) Acessar sistema
     3) Sair
     Selecione uma opcao: '''

usuarios = []
senhas = []

while True:
    opcao = input(menu)

    if opcao == 1:
        login = raw_input('Login: ')
        senha = raw_input('Senha: ')

        usuarios.append(login)
        senhas.append(senha)
    elif opcao == 2:
        login = raw_input('Insira login: ')
        senha = raw_input('Insira a senha: ')

        if login in usuarios:
            if senhas[usuarios.index(login)] == senha:
                print 'Logado com sucesso!'
                continue

        print 'Login ou senha invalidos'
    elif opcao == 3:
        print 'Ate logo'
        break