import gsd
from flask import Flask, render_template, make_response
from flask import request, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", string_variable="")


@app.route("/get-data", methods=["GET", "POST"])
def get_data():
    if request.method == "POST":
        try:
            req = request.form
            ticker = req.get("ticker")
            data = gsd.getStockData_string(ticker)
            # response = make_response(getKickstartFile())
            # response.headers["content-type"] = "text/plain"
        except:
            data = "TICKER NOT FOUND"

        return render_template("home.html", string_variable=data.split('\n'))

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
