import pandas as pd
import matplotlib.pyplot as plt
from json import loads, dumps
from flask import jsonify

def alleInfo(bestandsnaam):
  separator = ";"
  if bestandsnaam == "MARKTEN_NEW.csv":
    separator = ","
  bestand = pd.read_csv("csvfiles/" + bestandsnaam, sep=separator, encoding='latin-1')
  legelijst = []

  for i, ad in bestand.iterrows():
    legelijst.append(i)
  
  leegDataframe = bestand.loc[legelijst].copy()
  result = leegDataframe.to_json(orient="records")
  parsed = loads(result)

  return dumps(parsed, indent=4)