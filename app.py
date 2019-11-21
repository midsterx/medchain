from flask import Flask, render_template, flash, request, session, redirect, url_for, make_response, jsonify
from flask_restful import Resource, Api
import requests
import json

app = Flask(__name__)
app.secret_key = 'this is the end'
api = Api(app)
url = 'http://127.0.0.1:8000'

class Index(Resource):
    def get(self):
        return redirect(url_for('admin'))

api.add_resource(Index, '/')

class Admin(Resource):
    def get(self):
        return make_response(render_template('admin.html'))
        
api.add_resource(Admin, '/admin')

class GetManDetails(Resource):
    def post(self):
        res = requests.post(url + '/admin/getmandetails', json.dumps([request.form.get('manufacturer_option')]))
        print(res)
        return res

api.add_resource(GetManDetails, '/getmandetails')

class Manufacturer(Resource):
    def get(self):
        return make_response(render_template('manufacturer.html')) 
    # def post(self):
    #     request.post(url + '/manaddmedicine', {'man_id': ,'med_id': ,'quantity': ,'med_name': ,'man_date': ,'exp_date': })
        # returns a Batch Number

api.add_resource(Manufacturer, '/manufacturer')

class WholesalerPage(Resource):
    def get(self):
        return make_response(render_template('wholesaler.html'))

api.add_resource(WholesalerPage, '/wholesaler')

class WholesalerData(Resource):
    def get(self):
        request.get(url + '/')
        return make_response(200)
    def post(self):
        request.post(url + '/')
        return make_response(200)

api.add_resource(WholesalerData, '/wholesalerdata')

class Customer(Resource):
    def get(self):
        return make_response(render_template('customer.html'))
    # def post(self):

api.add_resource(Customer, '/customer')

    
if __name__ == '__main__':
	app.run()