#!/usr/bin/python

from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
from model_deployment import predict
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

api = Api(
    app, 
    version='1.0', 
    title='Price Prediction API',
    description='Price Prediction API')

ns = api.namespace('predict', 
     description='Price')
   
parser = api.parser()

# Definición API Flask
api = Api(
    app, 
    version='1.0', 
    title='Price Prediction API',
    description='Price Prediction API')

ns = api.namespace('predict', 
     description='Price')

# Definición argumentos o parámetros de la API
parser = api.parser()
#Year
parser.add_argument(
    'Year', 
    type=int, 
    required=True, 
    help='Year', 
    location='args')

#Mileage
parser.add_argument(
    'Mileage', 
    type=float, 
    required=True, 
    help='Mileage', 
    location='args')
#State
parser.add_argument(
    'State', 
    type=str, 
    required=True, 
    help='State', 
    location='args')
#Make
parser.add_argument(
    'Make', 
    type=str, 
    required=True, 
    help='Make', 
    location='args')
#Model
parser.add_argument(
    'Model', 
    type=str, 
    required=True, 
    help='Model', 
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.String,
})

# Definición de la clase para disponibilización
@ns.route('/')
class PhishingApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        return {
         "result": predict(args['Year'], args['Mileage'], args['State'], args['Make'], args['Model'])
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
