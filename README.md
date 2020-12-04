# This is a Geolocalization REST API
This api enables you to add, delete or provide geo-location data on the base of ip address or URL.<br>
I have build a postman collection which enables you to verify all the queries, it is available here: https://www.getpostman.com/collections/6e591fc1fbde3cccbf20

### Avaiable Endpoints:<br>
# /geo<br>
#### Available queries:<br>
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
POST with params:
```json
 {
    "auth": "<{'username': 'password'}>",
    "ip": "<ip>",
    "location": "<location>",
    "symbol": "<symbol>",
    "method": "method can be manual then you need to specify the ip details(location,symbol) or auto the details will be gethered from ipstack.com"
 }
```
exaple: https://geolocalization-api.herokuapp.com/geo?ip=134.201.250.155&location=Netherlands&symbol=NL&method=auto&auth={'dominik': 'password'}
example responses:
```json
{
    "message": "Successfully updated the record with automatic data",
    "data": [
        "United States",
        "US",
        "134.201.250.155",
        "auto"
    ]
}
```
```json
{
    "message": "Successfully updated the record with manual data",
    "data": {
        "ip": "134.201.250.155",
        "location": "Netherlands",
        "symbol": "NL",
        "method": "manual"
    }
}
```

#
DELETE with params:
```json
 {
    "auth": "<{'username': 'password'}>",
    "ip": "<ip>"
 }
```
exaple: https://geolocalization-api.herokuapp.com/geo?ip=134.201.250.155&auth={'dominik': 'password'}
example responses:
```json
{
    "message": "Successfully removed row",
    "data": "134.201.250.155"
}
```
#
# /ipAddres<br>
#### Available queries:<br>
GET with param:
```json
 {
    "auth": "<{'username': 'password'}>"
 }
```
exaple: https://geolocalization-api.herokuapp.com/ip/134.201.250.155?auth={'dominik': 'password'}
example responses:
```json
{
    "message": "Success",
    "data": [
        "134.201.250.155",
        "Netherlands",
        "NL"
    ]
}
```
#
DELETE with param:
```json
 {
    "auth": "<{'username': 'password'}>"
 }
```
exaple: https://geolocalization-api.herokuapp.com/ip/0.0.0.1?auth={'dominik': 'password'}
example responses:
```json
{
    "message": "Successfully removed row",
    "data": "0.0.0.1"
}
```
#
