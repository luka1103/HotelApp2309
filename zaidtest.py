import pandas as pd
import csv
import folium
from flask import Flask, render_template,jsonify, request



def fuctiezaid5zoek_in_csv(zoektekst):
    bestand = pd.read_csv("csvfiles/MuseaGalleries.csv", sep=";", encoding='latin-1')
    resultaat = bestand[bestand['Title'].str.contains(zoektekst, case=False, na=False)][['Title', 'Adres']].iloc[0]
    return resultaat

def functiezaid4index():
    return render_template('museum_map.html')

def functiezaid3zoek():
    zoeknaam = request.args.get('naam', '')
    bestand = pd.read_csv("csvfiles/MuseaGalleries.csv", sep=";", encoding='latin-1')
    geselecteerde_kolommen = ['Title', 'Shortdescription', 'Calendarsummary', 'City', 'Adres', 'Zipcode']
    resultaat = bestand[bestand['Title'].str.contains(zoeknaam, case=False)][geselecteerde_kolommen]
    resultaat_lijst = resultaat.to_dict(orient='records')

    return jsonify(resultaat_lijst)


def functiezaid2():
   keys = ('Latitude','Longitude')
   records = [ ]

   bestand = pd.read_csv("csvfiles/MuseaGalleries.csv", sep=";", encoding='latin-1')
   #print(bestand)
   data = bestand.to_dict(orient='records')
   museum_map = folium.Map(location=[52.377956, 4.897070], zoom_start=15)

   for row in data: 
        records.append({key: row[key] for key in keys})
        latitude = float(row['Latitude'].replace(',', '.'))
        longitude = float(row['Longitude'].replace(',', '.'))

        #print(records[0])
        NaamLocatie = row['Title']
        Adress = row['Adres']
        

        tooltip = f'{NaamLocatie}, {Adress}'

        folium.Marker([latitude, longitude], tooltip=tooltip).add_to(museum_map)
        museum_map.save('museum_map.html') 
functiezaid2()


