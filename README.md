#This is a Geolocalization REST API
This api enables you to add, delete or provide geo-location data on the base of ip address or URL.

##Avaiable Endpoints:
#####/geo
###Available queries:
GET with param:
```json
 {
    "auth": "{'username': 'password'}"
 }
```
exaple query: https://geolocalization-api.herokuapp.com/geo?auth={'dominik': 'password'}<br>
example response:
```json
{
    "message": "Success",
    "data": [
        [
            "0.0.0.0",
            "Poland",
            "PL"
        ],
        [
            "0.0.0.1",
            "Poland",
            "PL"
        ],
        [
            "0.0.0.2",
            "Germany",
            "GER"
        ]
    ]
}
```
#
POST with param:
```json
 {
    "auth": "<{'username': 'password'}>",
    "ip": "<ip>",
    "location": "<location>",
    "symbol": "<symbol>",
    "method": "<method>"
 }
```
exaple: https://geolocalization-api.herokuapp.com/geo?ip=134.201.250.155&location=Netherlands&symbol=NL&method=auto&auth={'dominik': 'password'}
example response:
```json
{
    "message": "Success",
    "data": [
        [
            "0.0.0.0",
            "Poland",
            "PL"
        ],
        [
            "0.0.0.1",
            "Poland",
            "PL"
        ],
        [
            "0.0.0.2",
            "Germany",
            "GER"
        ]
    ]
}
```
#