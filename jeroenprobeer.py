import pandas as pd
from json import loads, dumps

def jeroenfunctie(stad):

  bestand = pd.read_csv("csvfiles/EtenDrinken.csv", sep=";", encoding='latin-1')
  legelijst = []

  for i, ad in bestand.iterrows():
    if ad["City"].find(stad) >= 0:
      print("Yes")
      legelijst.append(i)
    else: 
      print("No")
  
  print(legelijst)
  leegDataframe = bestand.loc[legelijst].copy()
  print (leegDataframe)
  result = leegDataframe.to_json(orient="records")
  parsed = loads(result)
  return dumps(parsed, indent=4) 
print(jeroenfunctie("HAARLEM"))