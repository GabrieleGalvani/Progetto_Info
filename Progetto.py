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

covid = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv')
regioni =  gpd.read_file('/workspace/Progetto_Info/Reg01012021_g_WGS84.zip')
province = gpd.read_file('/workspace/Progetto_Info/ProvCM01012021_g_WGS84.zip')
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/Aosta', methods=['GET'])
def Aosta():
    return render_template("Aosta.html")

@app.route('/liguria.png', methods=['GET'])
def liguriapng():
    fig, ax = plt.subplots(figsize = (12,8))

    liguria.to_crs(epsg=3857).plot(ax=ax,facecolor='none', edgecolor="k")
    contextily.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/Liguria', methods=['GET'])
def Liguria():
    global liguria
    liguria = regioni[regioni["DEN_REG"] == "Liguria"]
    return render_template("Liguria.html")
    
@app.route('/Piemonte', methods=['GET'])
def Piemonte():
    return render_template("Piemonte.html")

@app.route('/Lombardia', methods=['GET'])
def Lombardia():
    return render_template('Lombardia.html')

@app.route('/Trentino', methods=['GET'])
def Trentino():
    return render_template('Trentino.html')

@app.route('/Veneto', methods=['GET'])
def Veneto():
    return render_template('Veneto.html')

@app.route('/Friuli', methods=['GET'])
def Friuli():
    return render_template('Friuli.html')

@app.route('/Emilia', methods=['GET'])
def Emilia():
    return render_template('Emilia.html')

@app.route('/Toscana', methods=['GET'])
def Toscana():
    return render_template('Toscana.html')

@app.route('/Marche', methods=['GET'])
def Marche():
    return render_template('Marche.html')

@app.route('/Umbria', methods=['GET'])
def Umbria():
    return render_template('Umbria.html')

@app.route('/Lazio', methods=['GET'])
def Lazio():
    return render_template('Lazio.html')



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)