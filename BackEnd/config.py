from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os
app = Flask(__name__) 
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
caminho = os.path.dirname(os.path.abspath(__file__))    
arquivobd = os.path.join(caminho, "novelas.db") 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+arquivobd 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
