import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
from scipy.sparse import load_npz


app = Flask(__name__)
gender_model = pickle.load(open('/app/gender_model.pkl', 'rb'))
age_model = pickle.load(open('/app/age_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    gender_test_data= load_npz('/app/X_test_gender.npz') 
    gender_prediction = gender_model.predict(gender_test_data[50:])
    gender_output = round(gender_prediction[0], 2)
    
    age_test_data=load_npz('/app/X_test_age.npz') 
    age_prediction = age_model.predict(age_test_data[50:])
    age_output = round(age_prediction[0], 2)
 
    return render_template('index.html', prediction_text='Gender and Age predictions for 50 Device ids {},{}'.format(gender_output,age_output))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
