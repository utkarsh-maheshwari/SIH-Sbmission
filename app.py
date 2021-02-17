from flask import Flask
from flask import render_template
from flask import request
import requests
from geopy.geocoders import Nominatim
import pandas as pd
import json
import main
#global result
app = Flask(__name__)
def getDM(json_object, name):
    for dict in json_object:
        if dict['District'] == name:
            return dict

@app.route("/dash", methods=["GET"])
def dash(result):
    geolocator = Nominatim(user_agent="SIH")
    lald = "26.8700, 80.9975"
    print("Latitude and Longitude:",lald)
    location = geolocator.geocode(lald)
    locaArr = str(location).split(",")
    zip = locaArr[len(locaArr)-2].strip()
    response = requests.get('https://api.postalpincode.in/pincode/'+zip)
    data = response.json()
    city = (data[0]['PostOffice'][0]['District'])
    with open('static/data/dmUP.json') as f:
        data = json.load(f)
    return render_template("dash.html",city=city)
    
@app.route("/map", methods=["GET"])
def map():
    return render_template("maps.html")

@app.route("/Hmap", methods=["GET"])
def Hmap():
    print(DP)
    print( DP[0])
    return render_template("Hmaps.html", lat = DP[0], long = DP[1],grid = Gr, cw = CW)

@app.route("/mapH", methods=["GET"])
def mapH():
    return render_template("maph.html")

@app.route("/data", methods=["GET","POST"])
def data():
    if request.method == "POST":
        global abc
        global DP, Gr, CW
        result = request.form
        abc = result
        Distress_time=result['Distress_time']
        Distress_position=result['Distress_position']
        if (Distress_position or Distress_time):
            Datum_point,Grid,Cell_Width=main.getData(result)
        if not(Distress_position and Distress_time):
            Datum_point,Datum_line,Grid,Cell_Width=main.getData(result)
        DP = Datum_point
        Gr = Grid
        CW = Cell_Width
        print(Datum_point,Grid,Cell_Width)
        return dash(result)
    if request.method == "GET":
        return render_template("dataCollect.html")
if __name__ == "__main__":
    app.run(debug=True)