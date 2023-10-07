# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:11:07 2023

@author: Luka
"""

import pandas as pd
import folium

def maakKaart():
   keys = ('Latitude','Longitude')
   records = [ ]
   bestand = pd.read_csv("csvfiles/MARKTEN_NEW.csv", sep=",", encoding="latin-1")
   data = bestand.to_dict(orient='records')

   museum_map = folium.Map(location=[52.377956, 4.897070], zoom_start=10)

   for row in data: 
        records.append({key: row[key] for key in keys})
        latitude = float(row['Latitude'])
        longitude = float(row['Longitude'])
        
        Artikelen = row['Artikelen']
        Dagen = row['FILTER_DAG'].replace('|', ' ')

        tooltip = f'Artikelen: {Artikelen} <br> Geopend op de volgende dagen: {Dagen}'
        
        if Artikelen.startswith('Algemene'):
         folium.Marker([latitude, longitude], tooltip=tooltip, icon=folium.Icon(color='blue', icon='store', prefix='fa')).add_to(museum_map)
        elif Artikelen.startswith('Kunst'):
         folium.Marker([latitude, longitude], tooltip=tooltip, icon=folium.Icon(color='purple', icon='palette', prefix='fa')).add_to(museum_map)
        elif Artikelen.startswith('Boeren'):
         folium.Marker([latitude, longitude], tooltip=tooltip, icon=folium.Icon(color='green', icon='tractor', prefix='fa')).add_to(museum_map)
        elif Artikelen.startswith('Boeken'):
         folium.Marker([latitude, longitude], tooltip=tooltip, icon=folium.Icon(color='gray', icon='book', prefix='fa')).add_to(museum_map)
        elif Artikelen.startswith('Postzegels'):
         folium.Marker([latitude, longitude], tooltip=tooltip, icon=folium.Icon(color='red', icon='envelope', prefix='fa')).add_to(museum_map)
        else:
         folium.Marker([latitude, longitude], tooltip=tooltip, icon=folium.Icon(color='orange', icon='seedling', prefix='fa')).add_to(museum_map)
        museum_map.save('templates/markten_kaart.html') 
