from flask import Flask, render_template, url_for , request , send_from_directory
import numpy as np
import math
import pickle

import os
import sys
import glob
from werkzeug.utils import secure_filename

app = Flask(__name__)


#Heart
model2 = pickle.load(open('heart_pred_model','rb'))





@app.route('/')
def index():
    return render_template('main.html')


@ app.route('/Heart')
def Heart():
    title = 'Heart'

    return render_template('first.html', title=title)






#Heart
@app.route("/predict2", methods=['POST'])
def predict2():
    if request.method == 'POST':
        Age= int(request.form['Age'])
        Sex = int(request.form['Sex'])
        CP = int(request.form['CP'])
        Trestbps = int(request.form['Trestbps'])
        
        Chol = int(request.form['Chol'])
        fbs=int(request.form['fbs'])
        Restecg = float(request.form['Restecg'])
        Thalach = float(request.form['Thalach'])
        Exang = int(request.form['Exang'])
        Oldpeak = float(request.form['Oldpeak'])
        Slope = int(request.form['Slope'])
        ca=int(request.form['ca'])
        Thal = int(request.form['Thal'])
        prediction = model2.predict([[Age,Sex,CP,Trestbps,Chol,fbs,Restecg,Thalach,Exang,Oldpeak,Slope,ca,Thal]])
        disease = 'Heart Disease'
        return render_template('after.html',data=prediction,disease = disease)



if __name__ == "__main__":
    app.run(debug=True)