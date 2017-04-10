from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.application import ApplicationModel

class Application(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('id',
        type=int,
        required=False,
        help="This field is not required"
    )
    parser.add_argument('firstname',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('lastname',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('ssn',
        type=int,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('employer',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('income',
        type=int,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('incomeFrequency',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('requestedAmount',
        type=int,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('requestedTerm',
        type=int,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('phoneNumber',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('emailAddress',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('isBranchEmployee',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('employeeID',
        type=int,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('lendercode',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    
    
    @jwt_required()
    def get(self, _id):
        application = ApplicationModel.find_by_id(_id)
        if current_identity.lendercode != '000' and current_identity.lendercode != application.lendercode:
            return {'Message': "You do not have access to that application. Application lendercode: {} and User lendercode: {}".format(application.lendercode, current_identity.lendercode)}, 401
        
        if application:
            return application.json(), 200
        return {"Message": "No application found with that ID."}, 404
        
    @jwt_required()
    def post(self):
        data = Application.parser.parse_args()
        if current_identity.lendercode != '000' and current_identity.lendercode != data['lendercode']:
            return {'Message': "You do not have access to submit to that lender. Application lendercode: {} and User lendercode: {}".format(data['lendercode'], current_identity.lendercode)}, 401
        
        appData = (
            data['firstname'],
            data['lastname'],
            data['ssn'],
            data['employer'],
            data['income'],
            data['incomeFrequency'],
            data['requestedAmount'],
            data['requestedTerm'],
            data['phoneNumber'],
            data['emailAddress'],
            data['isBranchEmployee'],
            data['employeeID'],
            data['lendercode'],
            "Submitted"
        )
        application = ApplicationModel(appData)
        application.getNewStatus()
        application.save_to_db()
        return {'Message': 'Application submitted successfully.', 'Application': application.json()}, 200
        
    @jwt_required()
    def put(self):
        data = Application.parser.parse_args()
        application = ApplicationModel.find_by_id(data['id'])
        if application == None:
            return {'Message': "Application with id of '{}' does not exist.".format(data['id'])}, 404
        if current_identity.lendercode != '000' and current_identity.lendercode != application.lendercode:
            return {'Message': "You do not have access to that application. Application lendercode: {} and User lendercode: {}".format(application.lendercode, current_identity.lendercode)}, 401
        
        application.firstname = data['firstname']
        application.lastname = data['lastname']
        application.ssn = data['ssn']
        application.employer = data['employer']
        application.income = data['income']
        application.incomeFrequency = data['incomeFrequency']
        application.requestedAmount = data['requestedAmount']
        application.requestedTerm = data['requestedTerm']
        application.phoneNumber = data['phoneNumber']
        application.emailAddress = data['emailAddress']
        application.isBranchEmployee = data['isBranchEmployee']
        application.employeeID = data['employeeID']
        application.lendercode = data['lendercode']
        application.status = "Re-Submitted"
        
        application.getNewStatus()
        application.save_to_db()
        return {'Message': 'Application re-submitted successfully.', 'Application': application.json()}, 200
        
    @jwt_required()
    def delete(self, _id):
        application = ApplicationModel.find_by_id(_id)
        if application == None:
            return {'Message': "Application with id of '{}' does not exist.".format(_id)}, 404
        if current_identity.lendercode != '000' and current_identity.lendercode != application.lendercode:
            return {'Message': "You do not have access to that application. Application lendercode: {} and User lendercode: {}".format(application.lendercode, current_identity.lendercode)}, 401
        
        if application:
            application.delete_from_db()
            
        return {'Message': 'Application deleted.'}, 200
            
        
class Applications(Resource):
    @jwt_required()
    def get(self, code):
        if current_identity.lendercode != '000' and current_identity.lendercode != code:
            return {'Message': "You do not have access to those applications. Attempted lendercode: {} and User lendercode: {}".format(code, current_identity.lendercode)}, 401
            
        return {'Results': ApplicationModel.find_by_lender(code)}