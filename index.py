# pylint: disable=print-statement

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ninja")
def ninjas():
    return render_template("ninja.html")

@app.route("/ninja/<ninjacolor>")
def ninjacolor(ninjacolor):
    if ninjacolor == "purple":
        return render_template("ninjapurple.html")
    if ninjacolor == "blue":
        return render_template("ninjablue.html")
    if ninjacolor == "red":
        return render_template("ninjared.html")
    if ninjacolor == "orange":
        return render_template("ninjaorange.html")
    else:
        return render_template("notapril.html")
    
app.run(debug=True)