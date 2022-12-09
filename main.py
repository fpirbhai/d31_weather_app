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
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10
    return {'station': station, 
            'date': date,
            'temperature': temperature
            }

@app.route("/api/v1/<station>")
def station_only(station):
    filename = 'Data\TG_STAID' + station.zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    return df.to_dict(orient='records')


@app.route("/api/v1/yearly/<station>/<year1>")
def station_year(station, year1):
    filename = 'Data\TG_STAID' + station.zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df.loc[df['    DATE'].str.startswith(str(year1))]
    return result.to_dict(orient='records')

if __name__ == "__main__":
    app.run(debug=True, port=5001)