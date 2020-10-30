from flask import Flask
from flask import request, jsonify
from joblib import load
import numpy as np
import pydash
from pydash import flatten



app = Flask(__name__)
model = load("tb_model.joblib")

@app.route("/", methods = ["POST","GET"])
def tb_status():
    patient_info  = request.get_json()["question"]
    patient_info_array = [patient_info]
    outcome = model.predict_proba(patient_info_array)
    outcome= np.ndarray.tolist(outcome)
    outcome = pydash.flatten_deep(outcome)
    
    return str(outcome[1])




