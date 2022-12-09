from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

stations = pd.read_csv('Data/stations.txt', skiprows= 17)

@app.route("/")
def home():
    return render_template("home.html", data = stations.iloc[:,0:2].to_html())



@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = 'Data\TG_STAID' + station.zfill(6) + '.txt'
    type_var = type(station)
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10
    return {'station': station, 
            'date': date,
            'temperature': temperature
            }


if __name__ == "__main__":
    app.run(debug=True, port=5001)