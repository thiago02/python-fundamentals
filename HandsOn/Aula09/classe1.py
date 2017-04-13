import psycopg2

class Conexao:
	con = None
	cur = None



	
	def conectar(self, host, db, user, passwd):
		self.con = psycopg2.connect(
			"host=%s dbname=%s user=%s password=%s" %
			(host, db, user, passwd)

		)
		self.cur = self.con.cursor()

	def sum(a,b):
		return a 


class Banco(Conexao):
	def __init__(self,host,db,user,passwd):
		self.conectar(host,db,user,passwd) 



	def find_one(self,id):
		self.cur.execute("SELECT * FROM posts WHERE id=%s" % id)
		return self.cur.fetchone()



objeto = Banco('localhost','projeto','postgres','123456')

print objeto.cur
print objeto.find_one(2)


