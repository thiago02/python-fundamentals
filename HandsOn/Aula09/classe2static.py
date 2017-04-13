import psycopg2

class Conexao:
	



	@staticmethod
	def conectar(host, db, user, passwd):
		con = psycopg2.connect(
			"host=%s dbname=%s user=%s password=%s" %
			(host, db, user, passwd)

		)
		cur = con.cursor()
		return con, cur


class Banco:
	con = None
	cur = None

	def __init__(self,host,db,user,passwd):
		self.con, self.cur = Conexao.conectar(host,db,user,passwd) 



	def find_one(self,id):
		self.cur.execute("SELECT * FROM posts WHERE id=%s" % id)
		return self.cur.fetchone()



objeto = Banco('localhost','projeto','postgres','123456')

print objeto.cur
print objeto.find_one(2)