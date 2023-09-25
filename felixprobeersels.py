import pandas
from json import loads, dumps
from flask import jsonify

def functiefelix(deparameter):
    bestand = pandas.read_csv("csvfiles/MARKTEN.csv",sep=';')
    for i, ad in bestand.iterrows():
        if ad["Locatie"].find(deparameter) == -1:
            bestand.drop(i, inplace=True)
    result = bestand.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4) 






def functiefelix2Netter(deparameter):
#    bestand = pandas.read_csv("csvfiles/EtenDrinken.csv",sep=';',encoding='latin-1')
    bestand = pandas.read_csv("csvfiles/MARKTEN.csv",sep=';')
#    bestand = pandas.read_csv("csvfiles/MuseaGalleries2.csv",sep=';', encoding='latin-1')
    leegDataframe = pandas.DataFrame(data=None, columns=bestand.columns, index=bestand.index).head(0)
    tekopieren = []

    for i, ad in bestand.iterrows():
        if ad["Locatie"].find(deparameter) > -1:
            tekopieren.append(i)

    leegDataframe = bestand.loc[tekopieren].copy()  
    result = leegDataframe.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4) 


print(functiefelix2Netter("Waterloo"))