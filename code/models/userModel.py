import sqlite3
from db import db
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    TABLE_NAME = 'users'

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return(cls.query.filter_by(username = username).first())


    @classmethod
    def find_by_id(cls, _id):
        return(cls.query.filter_by(id=_id).first())

    @classmethod
    def delete_from_db(cls, username ,password):
        current_user = cls.query.filter_by(username = username).first()
        if current_user == None:
            return {"message":"The username with current username does not exist."}
        else:
            if current_user.password == password:
                db.session.delete(current_user)
                db.session.commit()
                return {"message":"user completely deleted."}
            else:
                return {"message":"The password is wrong."}
    @classmethod
    def update_in_databse(cls, username , password, new_password):
        user = cls.query.filter_by(username=username).filter_by(password=password).first()
        if user:
            user.password = new_password
            db.session.add(user)
            db.session.commit()
            return{"message":"username successfully updated."}
        else:
            return {"message":"such user name does not exist."}
