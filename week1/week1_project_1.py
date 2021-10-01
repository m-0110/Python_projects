'''PROGRAM DESCRIPITON:
	Create a RESTFUL API Server in Python Flask. To achieve your target go through following process:-

    1) You have to hit the URL "https://api.thedogapi.com/v1/breeds" into a local JSON file into ur localhost.
    2) From the JSON file scrap the data of the breed of dog, country of origin,
        bred for which purpose and the image of the dog.
    3) Display the data in a tabular format into a HTML page.
    4) Send the extracted data into a MongoDB database with basic CRUD operations associated with it.

    jinja template to integrate python code and html
'''


#PROGRAMMED BY: Modika Ishwarya
#email-id:b18cs002@kitsw.ac.in
#DATE:21-09-2021
#PYTHON VERSION:3.8
#CAVEATS:None
#LICENSE:None





import requests
import json

from flask import Flask
from flask import render_template

import pymongo
from pymongo import MongoClient


from flask import jsonify
from flask import request


#for creating mongodb rest api using flask
from flask_pymongo import PyMongo


#create flask object
app = Flask(__name__)


#using mongodb and creating class to establish connection and perform operations
class Mongo_db:

    def __init__(self):
        self.connection=None

    #establish connection
    def establish_connection(self):

        self.connection=MongoClient("mongodb://localhost:27017/")
        if(self.connection):
            return True
        else:
            return False

    # getting list of databases
    def list_db(self):

        if(self.connection):
            return list(self.connection.list_database_names())


    #creating database
    def create_database(self,db_name):

        if (self.connection):
            #check exists or not by calling db_exists function

            if(self.db_exists(db_name)):
                print("database already exists")
            #if not exists create it
            else:
                my_db=self.connection[db_name]
                print(db_name,"created")


    #checking db exists or not
    def db_exists(self,db_name):

        if (self.connection):
            db_list = self.list_db()
            if(db_name in db_list):
                return True
            else:
                return False

    # create collection
    def create_new_collection(self, db_name, new_collection):

        if self.connection :
            db_name = self.connection[db_name]
            if(new_collection not in db_name.list_collection_names()):#if collection not exists create
                new_collection = db_name[new_collection]


    #insert extracted data into mongodb

    def insert(self,db_name,collection_name,breed):
        if self.connection:
            db_name = self.connection[db_name]
            new_collection = db_name[collection_name]
            for document in breed:
                new_collection.insert_one(document)
        else:
            return "error"

    #display documents in collection
    def display_collection(self,db_name,collection_name):
        if self.connection:

            db_name = self.connection[db_name]
            collection = db_name[collection_name]
            result=collection.find()

            print('documents in collection ',collection_name)
            for i in result:
                print(i)

        else:
            return "error"











#sending request to url
class test:

    def check_url(self, url):
        try:
            url = requests.get(url)
            return True
        except:
            return False

    def read_url(self, url):
        url = requests.get(url)
        return url.text

    def return_json(self, url):

        response = requests.get(url)
        if(response.status_code==200):
            print(' request is successful\n ')
            # response.json() method to see the data we received back from the API in json format
            return response.json()
        else:
            return -1








#scrape the data from json

def extract(file):
    breeds=[]# to store the scraped data

    with open("project1.json", "r") as file:
        data=json.load(file)
    k=0
    for d in data:
        breeds.append({}) #create dictionary for to store a document

        #store name
        if('name' in d ):
            breeds[k]['name']=d['name']

        #store breed_group
        if('breed_group' in d):
            breeds[k]['breed_group']=d['breed_group']

        #store bred_for
        if('bred_for' in d):
            lt=d['bred_for'].split(',')
            breeds[k]['bred_for'] = []
            for i in lt:

                breeds[k]['bred_for'].append(i.strip())

        #store origin
        if('origin' in d):
            lt = d['origin'].split(',')
            breeds[k]['origin'] = []
            for i in lt:
                breeds[k]['origin'].append(i.strip())

        #store image url
        if('image' in d and 'url' in d['image']):
            breeds[k]['image-url']=d['image']['url']

        #increment count of documents to store next document
        k+=1

    #return the scraped data
    return breeds









url = "https://api.thedogapi.com/v1/breeds"

s = test()
d1=""
d2=""
#checking url exists or not
if(s.check_url(url)):

    #get the response from api as json
    data=s.return_json(url)

    #dump into json file
    with open("project1.json", "w") as file:
        json.dump(data, file)
    file="project1.json"

    #scrap the data
    data_required=extract(file)




    # establish_connection create collections,insert

    s1 = Mongo_db()

    s1.establish_connection()
    database_name = "projects"
    s1.create_database(database_name)

    collection_name = "breeds_of_dog"
    s1.create_new_collection(database_name, collection_name)#create collection
    s1.insert(database_name,collection_name,data_required)#insert documents into database

    d1=['name','breed_group','bred_for','origin','image-url'] # column names to be passed to table .html
    d2=data_required



app.config['MONGO_DBNAME'] = 'projects'
app.config["MONGO_URI"] = "mongodb://localhost:27017/projects"
mongo = PyMongo(app)


#home page
@app.route('/')
def index():
    return render_template('index.html')

#table
@app.route('/breeds')
def home():
    return render_template('table.html', index=d1, rows=d2,upper=str.upper)

#create mongodb rest api to fetch data

@app.route('/display', methods=['GET'])
def display_collection():
    breeds = mongo.db.breeds_of_dog
    output = []
    data=breeds.find() #fetch data

    for s in data:
        s.pop("_id")
        output.append(s)
    #jsonify the output(list) having documents
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True,port=5000)


















