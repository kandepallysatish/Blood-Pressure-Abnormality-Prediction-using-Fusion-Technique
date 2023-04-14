import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
from sklearn.preprocessing import MinMaxScaler
from werkzeug.utils import secure_filename
import pickle
import webbrowser

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier


app = Flask(__name__) #Initialize the flask App


BoostedRFclassifier = pickle.load(open('BoostedRFclassifier.pkl','rb'))

@app.route('/')
@app.route('/first')
def first():
	return render_template('first.html')


@app.route('/login')
def login():
	return render_template('login.html')
    

@app.route('/prediction', methods = ['GET', 'POST'])
def prediction():
    return render_template('prediction.html')


@app.route('/predict',methods=['POST'])
def predict():
	int_feature = [x for x in request.form.values()]
	 
	final_features = [np.array(int_feature, dtype='float64')]
	 
	result = BoostedRFclassifier.predict(final_features)
	if result == 1:
			result = "Abnormal"
	else:
		result = 'Normal'
	return render_template('prediction.html', prediction_text= result)


@app.route('/performance')
def performance():
	return render_template('performance.html')   

#webbrowser.open('http://127.0.0.1:5000/', new=1)    

if __name__ == "__main__":
    app.run()
