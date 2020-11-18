from flask import Flask, jsonify, request
from flask_cors import CORS
from fastai import *
from fastai.text.all import *
import torch

app = Flask(__name__)
cors = CORS(app)
learner = load_learner("final-classifier-2.pkl", cpu=False)

@app.route('/')
def hello_world():
    return "Hello World"

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
    return jsonify(return_body)  #prediction[0]
  
if __name__ == '__main__':
    
    app.run(port=8000, debug=True)