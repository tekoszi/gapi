import os
import sqlite3
import markdown
import requests
import json
from flask import Flask
from flask_restful import Resource, Api, reqparse
import jwt

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


    def authVerify(self, auth):
        conn, c = self.dbConnect()
        token = jwt.encode(auth, 'secret', algorithm='HS256').decode("utf-8")
        c.execute('SELECT * FROM geo WHERE token=?', (token,))
        if c.fetchall():
            return True
        else:
            return False

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('auth', required=True)
        args = parser.parse_args()
        if self.authVerify(args['auth']):
            conn, c = self.dbConnect()
            c.execute("SELECT * FROM geo")

            return {'message': 'Success', 'data': c.fetchall()}
        else:
            return {'message': 'Failure', 'data': 'Unauthorized'}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ip', required=True)
        parser.add_argument('location')
        parser.add_argument('symbol')
        parser.add_argument('method', required=True)
        parser.add_argument('auth', required=True)
        args = parser.parse_args()
        if self.authVerify(args['auth']):
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
                try:
                    ipGeoData = self.getIpGeo(args['ip'])
                except Exception:

                    return {'message': 'The was a connection error to ipstack.com', 'data': []}
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
        else:
            return {'message': 'Failure', 'data': 'Unauthorized'}


    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ip', required=True)
        args = parser.parse_args()
        if self.authVerify(args['auth']):
            conn, c = self.dbConnect()
            c.execute('DELETE FROM geo WHERE ip=?', (args['ip'],))
            conn.commit()

            return {'message': 'Successfully removed row', 'data': args['ip']}
        else:
            return {'message': 'Failure', 'data': 'Unauthorized'}

class IpAddress(Resource):
    ...

api.add_resource(Geo, '/geo')
