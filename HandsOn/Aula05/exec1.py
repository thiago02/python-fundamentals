# ----- CONEXAO COM O BANCO
import psycopg2

con = psycopg2.connect(
	"host=%s dbname=%s user=%s password=%s" % (
	'localhost' , 'projeto' , 'postgres' , '123456'

	)
)
cur =con.cursor()
print con

# INSERIR UM POST 

conteudo = raw_input("digite o conteudo: ")
titulo = raw_input ("digite o titulo: ")
cur = con.cursor()
cur.execute(" \
INSERT INTO posts (conteudo, titulo) \
VALUES ('%s' , '%s' )" %(conteudo, titulo) )
con.commit


print cur.rowcount


# RECEBE CONTEUDO E TITULO

cur.execute("SELECT * FROM posts")

for row in cur.fetchall():
	print 'Conteudo: %s \n Titulo:  %s' %(
		row[1], row[2] 	)
	

#BUSCA UM POST

# RECEBE TRECHO DO TITULO 
id = raw_input ("digite um trecho na busca: ")

cur.execute("SELECT * FROM posts WHERE id= %s " % id)

row = cur.fetchone()



print "ID %s , Titulo %s, Conteudo %s" % (
		row[0], row[1], row[2] 
	)
