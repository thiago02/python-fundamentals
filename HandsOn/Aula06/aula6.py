import MySQLdb

con = MySQLdb.connect(
	host= '127.0.0.1', user='admin', passwd='4LINUX-THIAGO', db='projeto'
)

cur = con.cursor()

	
	#INSERT
try: 
	cur.execute(
		"INSERT INTO posts (titulo, conteudo) VALUES ('Meu titulo', 'Meu conteudo')"

	)
	con.commit()
except Exception as e:
	con.rollback()
#UPDATE
try:
	cur.execute(
		"UPDATE posts SET titulo= 'Novo titulo' WHERE id=1"
	)
	con.commit()
except Exception as e:
	con.rollback()

#SELECT ONE 
cur.execute('SELECT * FROM posts WHERE id=2'
	)

print cur.fetchone()

#SELECT ALL

cur.execute('SELECT * FROM posts '
)

for row in cur.fetchall():
	print row

cur.close()
