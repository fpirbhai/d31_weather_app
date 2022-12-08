from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/api/v1/<word>")
def result(word):
    return {'definition': word.upper(),
            'word': word}


if __name__ == "__main__":
   app.run(debug=True, port=5002) 
