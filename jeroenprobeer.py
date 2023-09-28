import pandas as pd
from json import loads, dumps

def jeroenfunctie(stad):

  bestand = pd.read_csv("csvfiles/EtenDrinken.csv", sep=";", encoding='latin-1')

  legelijst = []

  for i, ad in bestand.iterrows():
    if ad["City"].find(stad) >= 0:
      legelijst.append(i)
  
  leegDataframe = bestand.loc[legelijst].copy()
  result = leegDataframe.to_json(orient="records")
  parsed = loads(result)
  return dumps(parsed, indent=4) 