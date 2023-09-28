def functiezaid():
  print("ik heb een groot hoofd")
  return "return van Zaid functie"

import pandas as pd
import csv
import folium
from flask import Flask, render_template

@app.route('/zaid')
def home():
    return "Welkom bij Musea Galleries!"

@app.route('/museum_map')
def functiezaid():
   keys = ('Latitude','Longitude')
   records = [ ]

   bestand = pd.read_csv("csv/MuseaGalleries.csv", sep=";", encoding='latin-1')
   data = bestand.to_dict(orient='records')
   museum_map = folium.Map(location=[52.377956, 4.897070], zoom_start=15)

   for row in data: 
        records.append({key: row[key] for key in keys})
        latitude = float(row['Latitude'].replace(',', '.'))
        longitude = float(row['Longitude'].replace(',', '.'))

        
        NaamLocatie = row['Title']
        Adress = row['Adres']
        
        tooltip = f'{NaamLocatie}, {Adress}'

        folium.Marker([latitude, longitude], tooltip=tooltip).add_to(museum_map)
        museum_map.save('template/museum_map.html')
   return render_template('museum_map.html')

if __name__ == '__main__':
    app.run(debug=True)
functiezaid()
