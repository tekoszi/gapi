from flask import Flask
import os
import markdown
from flask_restful import Resource, Api
import sqlite3

app = Flask(__name__)
api = Api(app)

conn = sqlite3.connect('database.db')
c = conn.cursor()



@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) +'/README.md', 'r') as file:
        content = file.read()
        return markdown.markdown(content)


@app.route("/create")
def create():

    return 'add Hello World'


@app.route("/read")
def read():

    return 'add Hello World'

@app.route("/update")
def update():

    return 'add Hello World'


@app.route("/delete")
def delete():

    return 'add Hello World'

class Geo(Resource):
    def get(self):
        c.execute("SELECT * FROM geo")
        return {'message': 'Success', 'data': c.fetchall()}

api.add_resource(Geo,'/geo')

