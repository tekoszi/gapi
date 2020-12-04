import requests
import json

def getIpGeo(ip):
    url = f"http://api.ipstack.com/{ip}?access_key=8d2f138919484c7efdc78001f795814a"
    response = requests.request("GET", url)

    return json.loads(response.text)



print(getIpGeo('134.201.250.155'))