from app import db
# criando as tabelas do banco de dados

class User(db.Model): #traz um medelo de tabela padrão
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=true)#criando a culuna da tebela
    username = db.Column(db.String, unique=True) #o unique  que so pode ter este valor
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

#construtor, geralmente para especificar campos obrigatorios.
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
#monstra uma lista de usuario, ao ives de todos de uma vez
    def __repr__(self):
        return "<User %r" % self.username

class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)#Intger formato inteiro
    content = db.Column(db.Text)#Text formato de texto
    user_id = db.Column(db.Integer, db.ForeighKey('users.id'))#ForeighKey refenrecia na tabela "users" o id

    user = db.relationship('User', foreign_keys=user_id)#fazendo um ralcionamento com o usuario

    def __init__(self, content, user_id)    :
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "Post %r" % self.id

class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeighKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeighKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)