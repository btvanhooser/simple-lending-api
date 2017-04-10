from app import app
from db import db
from models.user import UserModel
from models.lender import LenderModel
import os

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all() 
    if UserModel.find_by_username('useradmin@000.com') is None:
        adminuser = UserModel('useradmin@000.com', '19513fdc9da4fb72a4a05eb66917548d3c90ff94d5419e1f2363eea89dfee1dd', '000')
        adminuser.save_to_db()
        webuser = UserModel('webuseradmin@000.com', '19513fdc9da4fb72a4a05eb66917548d3c90ff94d5419e1f2363eea89dfee1dd', '000')
    if LenderModel.find_by_lendercode('000') is None:
        lender = LenderModel('Admin Lender', '000')
        lender.save_to_db()
        lender = LenderModel('Software Developer Credit Union', '111')
        lender.save_to_db()
        lender = LenderModel('Orange County Credit Unionr', '222')
        lender.save_to_db()
        lender = LenderModel('Southern California Credit Union', '333')
        lender.save_to_db()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(host=host,port=port)