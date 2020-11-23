# -- coding: utf-8 --
#!/usr/bin/python3

from flask_cors import CORS, cross_origin
from pymongo import MongoClient
from flask import Flask, jsonify, request, escape

app = Flask(__name__)
cors = CORS(app)

# DB connectivity
client = MongoClient("mongodb+srv://bestcar:test123@bestcar.kgm2k.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.BestCar
collection_carros = db.carros

@app.route('/carros/', methods=['GET'])
@cross_origin()
def geral__():
    BestCar = collection_carros
    listCarro = []
    carros = BestCar.find()
    for j in carros:
        j.pop('_id')
        listCarro.append(j)
    return jsonify(listCarro)


@app.route('/carros/hatch', methods=['GET'])
@cross_origin()
def hatch__():
    BestCar = collection_carros
    listHatch = []
    hatch = BestCar.find({"categoria": "Hatch"})
    for j in hatch:
        j.pop('_id')
        listHatch.append(j)
    return jsonify(listHatch)


@app.route('/carros/sedan-compacto', methods=['GET'])
@cross_origin()
def sedanCompacto__():
    BestCar = collection_carros
    listSedanCompct = []
    SedanCompct = BestCar.find({"categoria": "Sedan Compacto"})
    for j in SedanCompct:
        j.pop('_id')
        listSedanCompct.append(j)
    return jsonify(listSedanCompct)

@app.route('/carros/sedan-medio', methods=['GET'])
@cross_origin()
def sedanMedio__():
    BestCar = collection_carros
    listSedanMedio = []
    SedanMedio = BestCar.find({"categoria": "Sedan Medio"})
    for j in SedanMedio:
        j.pop('_id')
        listSedanMedio.append(j)
    return jsonify(listSedanMedio)

@app.route('/carros/sedan-luxo', methods=['GET'])
@cross_origin()
def sedanLuxo__():
    BestCar = collection_carros
    listSedanLuxo = []
    SedanLuxo = BestCar.find({"categoria": "Sedan Luxo"})
    for j in SedanLuxo:
        j.pop('_id')
        listSedanLuxo.append(j)
    return jsonify(listSedanLuxo)

@app.route('/carros/picape-compacta', methods=['GET'])
@cross_origin()
def picapeCompacta__():
    BestCar = collection_carros
    listPicapeCompct = []
    PicapeCompct = BestCar.find({"categoria": "Picape Compacta"})
    for j in PicapeCompct:
        j.pop('_id')
        listPicapeCompct.append(j)
    return jsonify(listPicapeCompct)

@app.route('/carros/picape', methods=['GET'])
@cross_origin()
def picape__():
    BestCar = collection_carros
    listPicape = []
    Picape = BestCar.find({"categoria": "Picape"})
    for j in Picape:
        j.pop('_id')
        listPicape.append(j)
    return jsonify(listPicape)

@app.route('/carros/suv', methods=['GET'])
@cross_origin()
def Suv__():
    BestCar = collection_carros
    listSuv = []
    Suv = BestCar.find({"categoria": "Suv"})
    for j in Suv:
        j.pop('_id')
        listSuv.append(j)
    return jsonify(listSuv)

@app.route('/carros/suv-premium', methods=['GET'])
@cross_origin()
def SuvPremium__():
    BestCar = collection_carros
    listSuvPremium = []
    SuvPremium = BestCar.find({"categoria": "Suv Premium"})
    for j in SuvPremium:
        j.pop('_id')
        listSuvPremium.append(j)
    return jsonify(listSuvPremium)

@app.route('/carros/suv-luxo', methods=['GET'])
@cross_origin()
def SuvLuxo__():
    BestCar = collection_carros
    listSuvLuxo = []
    SuvLuxo = BestCar.find({"categoria": "Suv Luxo"})
    for j in SuvLuxo:
        j.pop('_id')
        listSuvLuxo.append(j)
    return jsonify(listSuvLuxo)

@app.route('/carros/monovolume', methods=['GET'])
@cross_origin()
def Monovolume__():
    BestCar = collection_carros
    listMonovolume = []
    Monovolume = BestCar.find({"categoria": "Monovolume"})
    for j in Monovolume:
        j.pop('_id')
        listMonovolume.append(j)
    return jsonify(listMonovolume)

@app.route('/carros/wagon', methods=['GET'])
@cross_origin()
def Wagon__():
    BestCar = collection_carros
    listWagon = []
    Wagon = BestCar.find({"categoria": "Wagon"})
    for j in Wagon:
        j.pop('_id')
        listWagon.append(j)
    return jsonify(listWagon)

@app.route('/carros/van', methods=['GET'])
@cross_origin()
def Van__():
    BestCar = collection_carros
    listVan = []
    Van = BestCar.find({"categoria": "Van"})
    for j in Van:
        j.pop('_id')
        listVan.append(j)
    return jsonify(listVan)


app.run('127.0.0.1', 3000, debug=True)
