import os
import sqlite3
import markdown
import requests
import json
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as file:
        content = file.read()

        return markdown.markdown(content)



class Geo(Resource):
    def getIpGeo(self, ip):
        url = f"http://api.ipstack.com/{ip}?access_key={os.environ['apikey']}"
        response = requests.request("GET", url)

        return json.loads(response.text)

    def dbConnect(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        return (conn, c)

    def get(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM geo")

        return {'message': 'Success', 'data': c.fetchall()}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ip', required=True)
        parser.add_argument('location')
        parser.add_argument('symbol')
        parser.add_argument('method', required=True)
        args = parser.parse_args()

        conn, c = self.dbConnect()
        c.execute('SELECT * FROM geo WHERE ip=?', (args['ip'],))

        if args['method'] == 'manual':
            if not c.fetchall():
                geoData = (args['ip'], args['location'], args['symbol'])
                c.execute('INSERT INTO geo VALUES (?,?,?)', geoData)
                conn.commit()
                return {'message': 'Successfully added new manual data', 'data': args}
            else:
                updateData = (args['location'], args['symbol'], args['ip'])
                c.execute("UPDATE geo SET location=?, symbol=? WHERE ip=?", updateData)
                conn.commit()
                return {'message': 'Successfully updated the record with manual data', 'data': args}

        elif args['method'] == 'auto':
            ipGeoData = self.getIpGeo(args['ip'])
            if not c.fetchall():
                geoData = (args['ip'], ipGeoData['country_name'], ipGeoData['country_code'])
                c.execute('INSERT INTO geo VALUES (?,?,?)', geoData)
                conn.commit()

                return {'message': 'Successfully added new automatic data', 'data': geoData}
            else:
                updateData = (ipGeoData['country_name'], ipGeoData['country_code'], args['ip'])
                c.execute("UPDATE geo SET location=?, symbol=? WHERE ip=?", updateData)
                conn.commit()

                return {'message': 'Successfully updated the record with automatic data', 'data': updateData}


api.add_resource(Geo, '/geo')
