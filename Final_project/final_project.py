import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


'''
PROGRAM DESCRIPTION:
Analysis of Auto Insurance claims and detect fraudulent claims
'''



#PROGRAMMED BY: Modika Ishwarya
#email-id:b18cs002@kitsw.ac.in
#DATE:21-10-2021
#PYTHON VERSION:3.8
#CAVEATS:None
#LICENSE:None

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for








#create flask object
app = Flask(__name__)

#home page
@app.route('/')
def index():
    return render_template('final_project.html')

#India
@app.route('/Data_Analysis')
def home():
    return render_template('fp1.html')

#World
@app.route('/Fraud_detection')
def home2():
    return render_template('fp2.html')
#PDF Page
@app.route('/pdf')
def home3():
    return render_template('fp3.html')
if __name__ == '__main__':
    app.run(debug=True, port=5000)
