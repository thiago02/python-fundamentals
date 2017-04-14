from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///banco.db') #caminho para selecionar o banco 
Base = declarative_base()

class Usuario(Base): 
	__tablename__ ='usuarios'
	id = Column(Integer, primary_key=True)
	nome = Column(String)





Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()   #session e uma variavel poderia ser qualquer nome

if __name__ == '__main__':
	try:
		for i in lista: 
			lista = raw_input("digite o nome do novo usuario:")



		usuario = Usuario(nome=lista) #cria um usuario no banco
		session.add(usuario)
		session.commit()
		#usuario = session.query(Usuario).get(1)
		#usuario = session.query(Usuario).all()
		#print session.query(Usuario).all()
		#print session.query(Usuario).filter_by(id=1, nome='gabriel').all() #ou .first()
		print usuario.nome, usuario.id
		#session.delete(usuario)
		session.commit()

	except Exception as e:
		print e 
		session.rollback()
