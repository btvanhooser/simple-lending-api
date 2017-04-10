from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.lender import LenderModel

class Lender(Resource):
    @jwt_required()
    def get(self):
        code = current_identity.lendercode
        lender = LenderModel.find_by_lendercode(code)
        if lender:
            return lender.json()
        return {'Message': "No lender with lendercode '{}' was found".format(code)}, 404
        
class Lenders(Resource):
    @jwt_required()
    def get(self):
        lenders = LenderModel.grab_all_lenders()
        return {'lenders': lenders}, 200