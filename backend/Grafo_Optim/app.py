
from flask import Flask, jsonify, request
import json 
import datetime
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS, cross_origin

# from analisis.analisis_algoritmo import *
# from sistemas_inteligentes.options_grafo import *
from sistemas_inteligentes.options_grafo import *
#manejo de errores al traer la informacion
class JSONEncoder(json.JSONEncoder):
	def default(self, o):
		if(isinstance(o, ObjectId)):
			return str(o)
		if(isinstance(o, datetime.datetime)):
			return str(o)	
		return json.JSONEncoder.default(self, o)

app = Flask(__name__)
#implementacion de CORS
CORS(app)

#conexion con MongoDB
#username = "admin"
#password = 0000
#name_bd = grafo_db
app.config['MONGO_URI'] = "mongodb+srv://admin:0000@cluster0.8fq1b.mongodb.net/grafo_db?retryWrites=true&w=majority"
app.config['MONGO_DBNAME'] = "grafo_db"
app.json_encoder = JSONEncoder
#app.config['MONGO_URI'] = "mongodb://localhost:27017/grafo_db"
mongo = PyMongo(app)

# implementacion cors
@cross_origin

@app.before_request
def before_request():
	print("Antes de la peticion...")

@app.after_request
def after_request(response):
	print("Despues de la peticion...")
	return response

@app.route('/grafos/analizar-grafo', methods=['POST'])
def analizar_grafo():
    if request.method == 'POST':
        #TODO: analizar grafo, guardar en MongoDB y retornar el nombre del grafo
        problema = request.json['problema']
        #String
        algoritmo = request.json['algoritmo']  # diccionario
        requerimiento = request.json['requerimientos']
        if problema != None:
            # analisis = Analisis_Algoritmo(grafo, option)
            # grafo_particion = analisis.get_grafo_particion()
            #print("si llego")
            solver_problema = Options_Grafo(problema, algoritmo, requerimiento)
            grafo_solucion = solver_problema.get_grafo_transform()
            #id = mongo.db.grafo_particion.insert_one(grafo_solucion)
            id = grafo_solucion #TODO: colocar id de grafo transformado y editado 
            return jsonify({'transaccion': True, "data":str(id)})
        return jsonify({'transaccion': False, "data":"No se ha podido procesar su solicitud"})

@app.route('/grafos/add-grafo', methods=['POST'])
def create_grafo():
	if request.method == 'POST':
		#receiving data
		id = mongo.db.grafo_registro.insert_one(request.json)
		return jsonify({'transaccion': True, "data":str(id)})
		
@app.route('/users/add-user', methods=['POST'])
def create_user():
	if request.method == 'POST':
		#receiving data
		id = mongo.db.user_registro.insert_one(request.json)
		return jsonify({'transaccion': True, "data":str(id)})

@app.route('/grafos/get-grafo/<id>', methods=['GET'])
def get_grafo(id):
    if request.method == 'GET':
		#receiving data
        #codigo es de grafo normal
        print(id)
        if(id.find('11111111')!=-1):
            print('es grafo normal')
            grafo = mongo.db.grafo_registro.find_one({"_id": id})
        else:
            print('es grafo particionado')
            #codigo es de grafo particionado
            grafo = mongo.db.grafo_particion.find_one({"_id": id})
        print(grafo)
        if grafo == None:
            return jsonify({'transaccion': False, "data": "No se encontro el Grafo"}),404
        return jsonify({'transaccion': True, "data":grafo})

@app.route('/users/get-user/<id>', methods=['GET'])
def get_user(id):
	if request.method == 'GET':
		#receiving data
		user = mongo.db.user_registro.find_one({"_id": id})
		if user == None :
			return jsonify({'transaccion': False, "data":"no se encontro usuario"}),404
		return jsonify({'transaccion': True, "data":user})

@app.route('/grafos/delete-grafo/<id>', methods=['DELETE'])
def delete_grafo(id):
	if request.method == 'DELETE':
		#receiving data
		status = mongo.db.grafo_registro.delete_one({"_id": id})
		return jsonify({'transaccion': True, 'data':str(status)})

@app.route('/grafos/delete-grafo-analizado/<id>', methods=['DELETE'])
def delete_grafo_a(id):
	if request.method == 'DELETE':
		#receiving data
		status = mongo.db.grafo_particion.delete_one({"_id": id})
		return jsonify({'transaccion': True, 'data':str(status)})

@app.route('/users/delete-user/<id>', methods=['DELETE'])
def delete_user(id):
	if request.method == 'DELETE':
		#receiving data
		status = mongo.db.user_registro.delete_one({"_id": id})
		return jsonify({'transaccion': True, 'data':str(status)})

@app.errorhandler(404)
def not_found(error):
	return jsonify({'error': 'Not found','url': request.url}), 404

@app.route('/grafos/listar-grafo', methods=['GET'])
def listar_grafo():
    if request.method == 'GET':
        data = mongo.db.grafo_registro.find({})
        listar_documentos = list(data)
        if data == None:
            return jsonify({'transaccion': False, "data":[]}),404
        return jsonify({'transaccion': True, "data":listar_documentos})

@app.route('/grafos/listar-grafo-analizado', methods=['GET'])
def listar_grafo_a():
    if request.method == 'GET':
        data = mongo.db.grafo_particion.find({})
        listar_documentos = list(data)
        if data == None:
            return jsonify({'transaccion': False, "data":[]}),404
        return jsonify({'transaccion': True, "data":listar_documentos})

@app.route('/users/listar-user', methods=['GET'])
def listar_user():
    if request.method == 'GET':
        data = mongo.db.user_registro.find({})
        listar_documentos = list(data)
        if data == None:
            return jsonify({'transaccion': False, "data": []}),404
        return jsonify({'transaccion': True, "data":listar_documentos})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)




