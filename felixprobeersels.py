import pandas

def functiefelix(deparameter):
    bestand = pandas.read_csv("csvfiles/EtenDrinken.csv",sep=';',encoding='latin-1')
#    bestand = pandas.read_csv("csvfiles/MARKTEN.csv",sep=';')
#    bestand = pandas.read_csv("csvfiles/MuseaGalleries2.csv",sep=';', encoding='latin-1')
    print(type(bestand))
    print(bestand.columns)

    for ad in bestand["Adres"]:
        print(ad)
    print(deparameter)
    return "return van felix functie"

print(functiefelix("fiets"))