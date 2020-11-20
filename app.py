from flask import Flask, jsonify, request
from flask_cors import CORS
from fastai import *
from fastai.text.all import *
import torch

app = Flask(__name__)
cors = CORS(app)
print("Loading machine learning model.")
learner = load_learner("final-classifier-2.pkl", cpu=True)
#learner = load_learner("/var/www/mscbackend/final-classifier-2.pkl", cpu=False)
print("Model loaded.")


@app.route('/predict', methods=['POST'])
def predict_controversy():
    json_body = request.json
    print(json_body)
    prediction = learner.predict(json_body)
    print(prediction)
    return jsonify({'prediction': True})  #prediction[0]

@app.route('/bulk-predict', methods=['POST'])
def bulk_predict_controversy():
    json_body = request.json
    return_body = {title:learner.predict(title)[0] for title in json_body}
    # prediction = learner.predict(json_body)
    # print(return_body)
	#response = jsonify(return_body)
	 #response.headers.add("Access-Control-Allow-Origin","*")
    return jsonify(return_body)  #prediction[0]


@app.route('/')
def hello_world():
    return 'Hello, World!'
