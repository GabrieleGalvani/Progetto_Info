# covid= https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv
from flask import Flask, render_template, send_file, make_response, url_for, Response,request,redirect
app = Flask(__name__)
# pip install flask pandas contextily geopandas matplotlib
import io
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/Aosta', methods=['GET'])
def aosta():
    return render_template("Aosta.html")

@app.route('/Liguria', methods=['GET'])
def Liguria():
    return render_template("Liguria.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)