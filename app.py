from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from models.user import UserModel
from models.lender import LenderModel
from resources.user import UserRegister, Users, WebUser
from resources.lender import Lender, Lenders
from resources.application import Application, ApplicationsByLender, ApplicationsByLastname, ApplicationsByFullname

import os, datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds = 3600)
app.secret_key = 'shaimus'
api = Api(app)

jwt = JWT(app, authenticate, identity)
        
api.add_resource(Lender, '/lender', '/lender/<string:lendercode>')
api.add_resource(Lenders, '/lenders')
api.add_resource(Application, '/application', '/application/<int:_id>')
api.add_resource(ApplicationsByLender, '/applications/<string:code>')
api.add_resource(ApplicationsByLastname, '/applications/<string:code>/<string:lastname>')
api.add_resource(ApplicationsByFullname, '/applications/<string:code>/<string:lastname>/<string:firstname>')
api.add_resource(UserRegister, '/user', '/user/<string:username>')
api.add_resource(Users, '/users/<string:lendercode>')
api.add_resource(WebUser, '/CreateTempWebUser')