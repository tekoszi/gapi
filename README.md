#This is a Geolocalization REST API
This api enables you to add, delete or provide geo-location data on the base of ip address or URL.

##Avaiable Endpoints:
#####/geo
###Available queries:
GET with param:
'''json
 {
    auth: "{'username': 'password'}"
 }
'''auth, exaple: https://geolocalization-api.herokuapp.com/geo?auth={'dominik': 'password'}
POST with params https://geolocalization-api.herokuapp.com/geo?ip=134.201.250.155&location=Netherlands&symbol=NL&method=auto&auth={'dominik': 'password'}