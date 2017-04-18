import psycopg2

con = psycopg2.connect("host=localhost dbname=dexter user=postgres password=123456")
cur = con.cursor()

def cadastrar_usuario():
    nome = raw_input('Nome: ')
    login = raw_input('Login: ')
    senha = raw_input('Senha: ')
    global cur, con
    try:
        cur.execute(" \
        INSERT INTO usuarios(nome, login, senha) \
        VALUES('%s', '%s', '%s')" % (nome, login, senha))

        if cur.rowcount:
            con.commit()
            return True
    except Exception as e:
        con.rollback()
        return False


def logar():
    global senhas, usuarios

    login = raw_input('Insira login: ')
    senha = raw_input('Insira a senha: ')

    if login in usuarios:
        if senhas[usuarios.index(login)] == senha:
            return True
    return False