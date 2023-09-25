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
    print(type(bestand))
    print(bestand.columns)
    print(bestand)
    leegDataframe = pandas.DataFrame()
    for i, ad in bestand.iterrows():
#    for ad in bestand["Adres"]:
        if ad["Locatie"] == deparameter:
            print("YES HIJ KOMT HIER")
        else:
            bestand.drop(i, inplace=True)

    print(leegDataframe)
    result = bestand.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4) 
    #return "return van felix functie"


print(functiefelix("Waterlooplein"))