# CRIAR UM LOOP QUE PEDE 4 OPCOES: 
# LOGAR
# INSERIR USUARIO
# BUSCAR USUARIO
# SAIR 
#
#
#

import psycopg2

flag= True
while flag:
	banner = '''Menu:
	1) Logar
	2) Inserir usuario
	3) Listar usuario 
	4) Sair 
	Selecione a opcao: '''

	a = int(raw_input(banner))

	if a ==1:
		print ("Opcao 1 selecionada ")
	elif a ==2: 
		print ("Opcao 2 selecionada ")
	elif a ==3:
		print ("Opcao 3 selecionada")
	elif a ==4:
		print ("Opcao 4 selecionada ") 
		flag = False 






