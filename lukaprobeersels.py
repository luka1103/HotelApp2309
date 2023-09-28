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