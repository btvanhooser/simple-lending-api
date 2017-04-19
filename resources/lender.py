from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.lender import LenderModel
from models.user import UserModel
from models.application import ApplicationModel
from werkzeug.security import safe_str_cmp

class Lender(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('id',
        type=int,
        required=False,
        help="This field is not required"
    )
    parser.add_argument('name',
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
    def get(self):
        code = current_identity.lendercode
        lender = LenderModel.find_by_lendercode(code)
        if lender:
            return lender.json(), 200
        return {'Message': "No lender with lendercode '{}' was found".format(code)}, 404
        
    @jwt_required()
    def post(self):
        data = Lender.parser.parse_args()
        if not safe_str_cmp(current_identity.lendercode, '000'):
            return {"Message": "You do not have the rights to create lenders. Please consult a member of (000) Admin Lender."}, 401
        if len(data['lendercode']) != 3:
            return {"Message": "Lendercode for a new lender must be 3 numbers."}, 400
        lender = LenderModel.find_by_lendercode(data['lendercode'])
        if lender:
            return {"Message": "A lender with that code already exists. Please use a lender that have a non-conflicting code."}, 304
        
        lender = LenderModel(data['name'], data['lendercode'])
        lender.save_to_db()
        return {"Message": "Lender created successfully."}, 201
        
    @jwt_required()
    def put(self):
        data = Lender.parser.parse_args()
        if not safe_str_cmp(current_identity.lendercode, '000'):
            return {"Message": "You do not have the rights to create lenders. Please consult a member of (000) Admin Lender."}, 401
        lender = LenderModel.find_by_id(data['id'])
        if lender is None:
            return {"Message": "No lender with id '{}' exists. Please create the lender before saving.".format(data['id'])}, 304
        if safe_str_cmp(lender.lendercode, '000'):
            return {"Message": "Lender 000 cannot be modified."}, 403
        if not safe_str_cmp(lender.lendercode, data['lendercode']):
            return {"Message": "Cannot change the lendercode of an already created lender."}, 400
        
        lender.name = data['name']
        lender.save_to_db()
        return {"Message": "Lender updated."}, 200
    
    @jwt_required()
    def delete(self, lendercode):
        if not safe_str_cmp(current_identity.lendercode, '000'):
            return {"Message": "You do not have the rights to create lenders. Please consult a member of (000) Admin Lender."}, 401
        lender = LenderModel.find_by_lendercode(lendercode)
        if lender is None:
            return {"Message": "No lender with lendercode '{}' exists.".format(lendercode)}, 304
        if safe_str_cmp(lendercode, '000'):
            return {"Message": "Lender 000 cannot be deleted."}, 403
        
        try:
            UserModel.delete_all_by_lendercode(lendercode)
            ApplicationModel.delete_all_by_lendercode(lendercode)
            lender.delete_from_db()
            return {"Message": "Lender and all related users/applications were deleted successfully."}, 200
        except RuntimeError:
            return {"Message": "Problem deleting. Please try again. Error: " + ReferenceError.message}, 500
        
class Lenders(Resource):
    @jwt_required()
    def get(self):
        lenders = LenderModel.grab_all_lenders()
        return {'Lenders': lenders}, 200