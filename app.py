from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from models.user import UserModel
from models.lender import LenderModel
from resources.user import UserRegister
from resources.lender import Lender, Lenders
from resources.application import Application, Applications

import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'shaimus'
api = Api(app)

jwt = JWT(app, authenticate, identity)
        
api.add_resource(Lender, '/lender')
api.add_resource(Lenders, '/lenders')
api.add_resource(Application, '/application', '/application/<int:_id>')
api.add_resource(Applications, '/applications/<string:code>')
api.add_resource(UserRegister, '/register')