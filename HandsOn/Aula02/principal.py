from Usuarios.Usuarios import *
from servidores.servidores import *

while True:
    menu = '''     -= Sistema =-
     1) Cadastrar usuario
     2) Acessar sistema
     3) Sair
     Selecione uma opcao: '''

    opcao = input(menu)

    if opcao == 1:
        if cadastrar_usuario():
            print  'Usuario cadastrado com sucesso!'
    elif opcao == 2:
        if logar():
            print 'Logado com sucesso!'
        else:
            print 'Login ou senha invalidos'
    elif opcao == 3:
        print 'Ate logo'
        break