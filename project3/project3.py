import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


'''
PROGRAM DESCRIPTION:
You have been given a CSV file of Death Mortality rates of world till 2019. You task is 
to do the following:-
1) Develop a Python Flask application for the project.
2) Display all the details like Graphs, Detailed extracted values from the CSV file 
for the same.
3) Display all the graphs using Matplotlib into the frontend using HTML, CSS, 
Javascript and Bootstrap with appropriate routes.
4) Use Linear Regression, Polynomial regression and Multiple Regression with RSquare, Coefficient of R and other statistical analysis tools on the data.
5) Use appropriate HTML, CSS, Javascript and Bootstrap tags for your project.
6) Create a full analytical report of your entire report and display it on the frontend 
with a PDF of it
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
    return render_template('project3.html')

#India
@app.route('/India')
def home():
    return render_template('page2.html')

#World
@app.route('/world')
def home2():
    return render_template('page3.html')
#PDF Page
@app.route('/pdf')
def home3():
    return render_template('page4.html')
if __name__ == '__main__':
    app.run(debug=True, port=5000)