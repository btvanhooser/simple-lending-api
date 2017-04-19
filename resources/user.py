from flask_restful import Resource, reqparse
from models.user import UserModel
from werkzeug.security import safe_str_cmp
from flask_jwt import jwt_required, current_identity
from random import randint
import datetime


class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('lendercode',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    
    @jwt_required()
    def post(self):
        if not safe_str_cmp(current_identity.lendercode,'000'):
            return {"Message": "Must be a 000 lender user to make changes to user database."}, 401
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {"message": "User already exists!"}, 400
        
        user = UserModel(data['username'], data['password'], data['lendercode'])
        user.save_to_db()
        
        return {"message": "User created successfully."}, 201
    
    @jwt_required()
    def put(self):
        if not safe_str_cmp(current_identity.lendercode, '000'):
            return {"Message": "Must be a 000 lender user to make changes to user database."}, 401
        data = UserRegister.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user is None:
            return {"Message": "User doesn't exist."}, 404
        if safe_str_cmp(user.lendercode, '000') and not safe_str_cmp(data['lendercode'], '000'):
            return {"Message": "000 users cannot have their lendercodes changed."}, 403
            
        user.password = data['password']
        user.lendercode = data['lendercode']
        return {"Message": "User updated successfully."}, 200
    
    @jwt_required()
    def delete(self, username):
        if not safe_str_cmp(current_identity.lendercode, '000'):
            return {"Message": "Must be a 000 lender user to make changes to user database."}, 401
        user = UserModel.find_by_username(username)
        if user is None:
            return {"Message": "User doesn't exist."}, 404
        if safe_str_cmp(user.username, current_identity.username):
            return {"Message": "Unable to make changes to self."}, 403
        if safe_str_cmp(user.username,'useradmin@000.com'):
            return {"Message": "You are not permitted to delete the root 'useradmin@000.com' as that is the system admin"}, 400
            
        user.delete_from_db()
        return {"Message": "User successfully removed from database."}, 200
        
class Users(Resource):
    
    @jwt_required()
    def get(self, lendercode):
        if not safe_str_cmp(current_identity.lendercode,'000') and not safe_str_cmp(current_identity.lendercode, lendercode):
            return {"Message": "You do not have permission to grab the users for this lender."}, 401
        users = UserModel.get_users_by_lendercode(lendercode)
        return {"Users": users}, 200
        
class WebUser(Resource):
    
    def get(self):
        uniqueName = str(datetime.datetime.now())
        password = randint(10000000,99999999)
        lendercode = "1"
        webuser = UserModel(uniqueName, password, lendercode)
        webuser.save_to_db()
        
        UserModel.check_temp_users();
        
        return {'username': webuser.username, 'password': webuser.password}, 200