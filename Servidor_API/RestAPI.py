# coding=utf-8
import requests
import os
from flask import Flask, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS
from Models.DB.DB_helper import INIT_API, Company
from Models.DAO import company_DAO
from Views import(vehicle_view, company_view, deliveryman_view,
address_view, client_view, package_view, delivery_view, service_order_view, login_view,
area_view)
#from test.teste import teste

UPLOAD_FOLDER = "/photo/"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#teste()
INIT_API()
CORS(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_photo/<id_user>', methods=['POST'])
def upload_file(id_user):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            response = {'error' : 'not file in request'}
            return jsonify(response), 400
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            response = {'error' : 'not selected file'}
            return jsonify(response), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            '''url_photo= 'url da foto aqui'
            dao = company_DAO()
            company = Company()
            company.id = id_user
            company.photo_url = url_photo
            dao.update(company)'''
            
            response = {'photourl' : 'retornar url da fota aqui'}
            return jsonify(response), 200
        

@app.route('/cnpj/<cnpj>',methods=['GET'])
def cnpj(cnpj):
    if request.method == 'GET':

        r = requests.get('https://www.receitaws.com.br/v1/cnpj/'+ str(cnpj) )

        return jsonify(r.json())

if __name__ == '__main__' :
    vehicle_view.initialize_view(app)
    company_view.initialize_view(app)
    deliveryman_view.initialize_view(app)
    address_view.initialize_view(app)
    client_view.initialize_view(app)
    package_view.initialize_view(app)
    delivery_view.initialize_view(app)
    service_order_view.initialize_view(app)
    login_view.initialize_view(app)
    area_view.initialize_view(app)
    app.run()
