menu = '''     -= Sistema =-
     1) Cadastrar usuario
     2) Acessar sistema
     3) Sair
     Selecione uma opcao: '''

usuarios = []
senhas = []
login = None
senha = None

def Cadastrar(a,b):
    global login
    global senha
    login = raw_input('Login: ')
    senha = raw_input('Senha: ')
    usuarios.append(login)
    senhas.append(senha)
    raw_input('usuario cadastrado com sucesso')

def Acessar(a,b):
    login = raw_input('Insira login: ')
    senha = raw_input('Insira a senha: ')






while True:
    opcao = input(menu)

    if opcao == 1:
        Cadastrar(login,senha)

        
    elif opcao == 2:
        Acessar(login,senha)




        if login in usuarios:
            if senhas[usuarios.index(login)] == senha:
                print 'Logado com sucesso!'
                continue

        print 'Login ou senha invalidos'
    elif opcao == 3:
        print 'Ate logo'
        break