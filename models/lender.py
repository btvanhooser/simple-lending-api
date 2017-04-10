from db import db

class LenderModel(db.Model):
    
    __tablename__ = 'lenders'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    lendercode = db.Column(db.String(5))
    
    def __init__(self, name, lendercode):
        self.name = name
        self.lendercode = lendercode
        
    @classmethod
    def find_by_lendercode(cls, lendercode):
        return cls.query.filter_by(lendercode=lendercode).first()
        
    @classmethod
    def grab_all_lenders(cls):
        return list(map(lambda x: x.json(), cls.query.all()))
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete()
        db.session.commit()
        
    def json(self):
        return {"name": self.name, "lendercode": self.lendercode}