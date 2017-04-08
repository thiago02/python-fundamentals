# ----- CONEXAO COM O BANCO
import psycopg2

con = psycopg2.connect(
	"host=%s dbname=%s user=%s password=%s" % (
	'localhost' , 'projeto' , 'postgres' , '123456'

	)
	print psycopg2.connect

)


# INSERIR UM POST 

cur = con.cursor()
cur.execute(" \
INSERT INTO posts (conteudo, titulo) \
VALUES ('a crise na china' , 'teste bla bla bla' )" )

if cur.rowcount:
	print "registro inserido com sucesso"
	cur= commit()

# RECEBE CONTEUDO E TITULO




#BUSCA UM POST




# RECEBE TECHO DO TITULO 