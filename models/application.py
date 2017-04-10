from werkzeug.security import safe_str_cmp
from db import db

class ApplicationModel(db.Model):
    
    __tablename__ = 'applications'
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    ssn = db.Column(db.Integer)
    employer = db.Column(db.String(80))
    income = db.Column(db.Integer)
    incomeFrequency = db.Column(db.String(80))
    requestedAmount = db.Column(db.Integer)
    requestedTerm = db.Column(db.Integer)
    phoneNumber = db.Column(db.String(80))
    emailAddress = db.Column(db.String(80))
    isBranchEmployee = db.Column(db.String(80))
    employeeID = db.Column(db.Integer)
    lendercode = db.Column(db.String(80))
    status = db.Column(db.String(80))
    
    def __init__(self, properties):
        self.firstname = properties[0]
        self.lastname = properties[1]
        self.ssn = properties[2]
        self.employer = properties[3]
        self.income = properties[4]
        self.incomeFrequency = properties[5]
        self.requestedAmount = properties[6]
        self.requestedTerm = properties[7]
        self.phoneNumber = properties[8]
        self.emailAddress = properties[9]
        self.isBranchEmployee = properties[10]
        self.employeeID = properties[11]
        self.lendercode = properties[12]
        self.status = properties[13]
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commmit()
    
    def getNewStatus(self):
        if safe_str_cmp(self.incomeFrequency, 'monthly'):
            monthlyIncome = self.income
        elif safe_str_cmp(self.incomeFrequency, 'yearly'):
            monthlyIncome = self.income/12
        elif safe_str_cmp(self.incomeFrequency, 'biweekly'):
            monthlyIncome = self.income*2
        else:
            monthlyIncome = self.income*4
        
        monthlyCost = self.requestedAmount * 1.0/self.requestedTerm
        
        if (safe_str_cmp(self.isBranchEmployee, 'yes')) and (self.employeeID > 100 and self.employeeID < 999):
            if monthlyCost < (monthlyIncome * .15):
                self.status = 'Approved'
            elif monthlyCost < (monthlyIncome * .25):
                self.status = 'Refer'
            else:
                self.status = 'Decline'
        else:
            if monthlyCost < (monthlyIncome * .10):
                self.status = 'Approved'
            elif monthlyCost < (monthlyIncome * .18):
                self.status = 'Refer'
            else:
                self.status = 'Decline'
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod    
    def find_by_lender(cls, lendercode):
        return list(map(lambda x: x.json(), cls.query.filter_by(lendercode=lendercode).order_by(cls.id.desc()).all()))
        
    def json(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "ssn": self.ssn,
            "employer": self.employer,
            "income": self.income,
            "incomeFrequency": self.incomeFrequency,
            "requestedAmount": self.requestedAmount,
            "requestedTerm": self.requestedTerm,
            "phoneNumber": self.phoneNumber,
            "emailAddress": self.emailAddress,
            "isBranchEmployee": self.isBranchEmployee,
            "employeeID": self.employeeID,
            "lendercode": self.lendercode,
            "status": self.status
        }