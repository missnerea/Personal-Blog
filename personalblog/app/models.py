from . import db 
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
	__tablename__='users'

	id = db.Column(db.Integer, primary_key = True )
	username = db.Column(db.String(255))
	email = db.Column(db.String(255), unique = True, index= True)
	pass_secure = db.Column(db.String(255))
	pass_hash = db.Column(db.String(255))
	bio = db.Column(db.String(255))
	profile_pic_path = db.Column(db.String(255))
	post = db.relationship("Post", backref="user", lazy = "dynamic")
	comment = db.relationship("Comment", backref="user", lazy = "dynamic")

		@property
        def password(self):
            raise AttributeError('You cannot read the password attribute')

        @password.setter
        def password(self, password):
            self.pass_secure = generate_password_hash(password)


        def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

class Roles(db.Model):
	__tablename__ = 'roles'

	id= db.Column(db.Integer, primary_key= True)
	name= db.Column(db.String(255))
	default = db.Column(db.Boolean, default= False , index= True)
	permissions = db.Column(db.Integer)
	user_id = db.relationship(db.Integer, db.ForeignKey('users.id'))

class Post(db.Model):
	__tablename__ = 'posts'

	id= db.Column(db.Integer, primary_key= True)
	name = db.Column(db.String(255))
	user_id= db.relationship(db.Integer,db.ForeignKey('users.id'))
	comment_id=db.relationship(db.Integer,db.ForeignKey('comments.id'))

class Comment(db.Model):
	id=db.Column(db.Integer, primary_key= True)
	name=db.Column(db.String(255))
	user_id= db.relationship(db.Integer,db.ForeignKey('users.id'))
	post_id= db.relationship(db.Integer,db.ForeignKey('posts.id'))

