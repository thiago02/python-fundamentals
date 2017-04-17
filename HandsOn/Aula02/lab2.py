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
    global usuarios
    global senhas
    global login
    global senha
   


    login = raw_input('Login: ')
    senha = raw_input('Senha: ')
    usuarios.append(login)
    senhas.append(senha)
    raw_input('usuario cadastrado com sucesso')

    return True 
    

def Acessar(a,b):
    global usuarios
    global senhas
    global login
    global senha
    login = raw_input('Insira login: ')
    senha = raw_input('Insira a senha: ')

    if login in usuarios:
        if senhas[usuarios.index(login)] == senha:
            return True
    return False
    





while True:
    opcao = input(menu)

    if opcao == 1:
        Cadastrar(login,senha)

        
    elif opcao == 2:
        if Acessar(login,senha):

            print 'Logado com sucesso!'
        
        else:
            print 'Login ou senha invalidos'
                        
    elif opcao == 3:
        print 'Ate logo'
        break