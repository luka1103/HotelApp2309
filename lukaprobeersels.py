import pandas as pd
import matplotlib.pyplot as plt
from json import loads, dumps
from flask import jsonify

def functieluka(artikelen):

  bestand = pd.read_csv("csvfiles/MARKTEN.csv", sep=";", encoding='latin-1')
  legelijst = []

  for i, ad in bestand.iterrows():
    if ad["Artikelen"].find(artikelen) >= 0:
      legelijst.append(i)
  
  leegDataframe = bestand.loc[legelijst].copy()
  result = leegDataframe.to_json(orient="records")
  parsed = loads(result)
  return dumps(parsed, indent=4) 

## De functies hieronder worden momenteel niet gebruikt.

def functieluka2(straat=None):
    bestand_markten = pd.read_csv("csvfiles/MARKTEN.csv", sep=";")
    bestand_restaurants = pd.read_csv("csvfiles/EtenDrinken.csv", encoding="latin-1", sep=";")
    leegDataframe = pd.DataFrame(data=None, columns=bestand_restaurants.columns, index=bestand_restaurants.index).head(0)
    tekopieren = []

    for i, ad in bestand_restaurants.iterrows():
        if ad["Adres"].startswith(straat) == True:
            tekopieren.append(i)

    leegDataframe = bestand_restaurants.loc[tekopieren].copy()  
    result = leegDataframe.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4) 

def functieluka3(straat=None):
    long_list = []
    lat_list = []
    bestand = pd.read_csv("csvfiles/MARKTEN.csv", sep=";")

    for long in bestand["WKT_LNG_LAT"]:
        first_number = ""
        for char in long:
            # Check if the character is a digit or a period
            if char.isdigit() or char == '.':
                first_number += char
            elif char == ' ':
                break
        long_list.append(float(first_number))

    for lat in bestand["WKT_LAT_LNG"]:
        first_number = ""
        for char in lat:
        # Check if the character is a digit or a period
            if char.isdigit() or char == '.':
                first_number += char
            elif char == ' ':
                break
        lat_list.append(float(first_number))
    
    plt.scatter(x=long_list, y=lat_list)
    plt.savefig('/static/images/new_plot.png')
    plt.close()
    return render_template('untitled1.html', name = 'new_plot', url ='/static/images/new_plot.png')