from db import db
from datetime import datetime

class UserModel(db.Model):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    lendercode = db.Column(db.String(5))
    
    def __init__(self, username, password, lendercode):
        self.username = username
        self.password = password
        self.lendercode = lendercode
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    def check_expired(self):
        datenow = datetime.now()
        checkdate = datetime.strptime(self.username, "%Y-%m-%d %H:%M:%S.%f")
        #2017-04-17 07:15:58.902764
        diff = datenow - checkdate
        print(str(diff.seconds))
        if diff.seconds > 1800:
            self.delete_from_db()
            print("deleted")
    
    @classmethod    
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
        
    @classmethod    
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        
    @classmethod
    def get_users_by_lendercode(cls, lendercode):
        return list(map(lambda x: x.json(), cls.query.filter_by(lendercode=lendercode).all()))
        
    @classmethod
    def delete_all_by_lendercode(cls, lendercode):
        map(lambda x: x.delete_from_db(), cls.query.filter_by(lendercode=lendercode).all())
        return
    
    @classmethod
    def check_temp_users(cls):
        list(map(lambda x: x.check_expired(), cls.query.filter_by(lendercode='1').all()))
    
    def json(self):
        return {"id": self.id, "username": self.username, "lendercode": self.lendercode}