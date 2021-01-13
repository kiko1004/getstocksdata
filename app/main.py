import gsd
from flask import Flask, render_template, make_response
from flask import request, redirect
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", string_variable="")

@app.route("/index.html")
def index():
    return render_template("index.html", string_variable="")

@app.route("/get-data", methods=["GET", "POST"])
def get_data():

    if request.method == "POST":
        try:
            req = request.form
            ticker = req.get("ticker")
            data = gsd.getStockData_string(ticker)
            a = gsd.getA(ticker)
            # response = make_response(getKickstartFile())
            # response.headers["content-type"] = "text/plain"
            spliteddata = data.split('\n')
            i = 0
            lables = []
            values = []
            while i<len(spliteddata):
                if  i%2==0:
                    lables.append(spliteddata[i])
                else: values.append(spliteddata[i])
                i+=1

            ziper = zip(lables, values)
            ziper = dict(ziper)



        except:
            data = "TICKER NOT FOUND"

        return render_template("index.html", string_variable=data.split('\n'), a_data = a, labels = lables, values=values, ziper = ziper)

    return render_template("index.html")



