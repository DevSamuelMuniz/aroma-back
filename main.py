from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["https://senac-aromaessence.netlify.app"]}})  

# Configuração do MongoDB
client = MongoClient('mongodb+srv://recinproj:NRdhqU14UA14vJF5@cluster0.r8fkm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['aroma_essence'] 
agendamentos_collection = db.agendamentoAroma

@app.route("/submit", methods=["POST"])
def submit_form():
    data = request.json
    if data:
        # Insere os dados recebidos no MongoDB
        agendamentos_collection.insert_one(data)
        return jsonify({"message": "Formulário enviado com sucesso!"}), 201
    else:
        return jsonify({"error": "Nenhum dado recebido"}), 400


if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0', port=port, debug=True)