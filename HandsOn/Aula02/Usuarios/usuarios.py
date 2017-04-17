usuarios = []
senhas = []

def logar():
    global senhas, usuarios

    login = raw_input('Insira login: ')
    senha = raw_input('Insira a senha: ')

    if login in usuarios:
        if senhas[usuarios.index(login)] == senha:
            return True
    return False


def cadastrar_usuario():
    global senhas, usuarios

    login = raw_input('Login: ')
    senha = raw_input('Senha: ')

    usuarios.append(login)
    senhas.append(senha)
    return True