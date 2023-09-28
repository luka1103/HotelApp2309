import pandas as pd
from json import loads,dumps

def search_csv_for_keywords(invoer):
    try:
        
    #Het CSV bestand lezen en in een DataFrame stoppen
        
        bestand = pd.read_csv("/Users/jeroenhadderingh/Desktop/hotelapp2309/HotelApp2309/csvfiles/TA_restaurants_curated.csv")
        lijstid = []
        
    #De gebruiker prompten om keywords in te vullen
    
        keywords_input = invoer
        
    #Lege DataFrame maken om de rijen op te slaan
    
        results_dataframe = pd.DataFrame(columns=bestand.columns)
        
    #Door de dataframe heen loopen op zoek naar keywords in cuisine styles
        for index, row in bestand.iterrows():
            #city= str(row.get("City", "")).lower()
            cuisine_style = str(row.get("Cuisine Style", "")).lower()
            
            if keywords_input in cuisine_style:
                lijstid.append(index)
        results_dataframe = bestand.loc[lijstid].copy()
            
    #rijen weergeven
        if not results_dataframe.empty:
            print("\nMatching Rows:")
            print(results_dataframe)
        else:
                print("\nNo matching rows found.")
                
    #error handling            
    except FileNotFoundError:
       print(f"Error: the file '{csv_file} does not exist'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
                
    result = results_dataframe.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4)           