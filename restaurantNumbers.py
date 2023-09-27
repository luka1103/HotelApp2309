import pandas as pd
import matplotlib.pyplot as plt

def restaurantNumbers(data_file_path, rating_treshold=4.0):

  bestand = pd.read_csv("/Users/jeroenhadderingh/Desktop/hotelapp2309/HotelApp2309/csvfiles/TA_restaurants_curated.csv")
  highly_rated_restaurants= bestand[bestand["Rating"] > rating_treshold]
  city_counts = highly_rated_restaurants["City"].value_counts()
  
  
  city_counts.plot(kind="bar", color="blue")
  plt.xlabel("City")
  plt.ylabel("Number of restaurants")
  plt.title("Number of highly rated restaurants in cities of Hotel X")
  plt.xticks(rotation=55, ha="right")
  plt.show()
  
  
  return city_counts
  
data_file_path = "/Users/jeroenhadderingh/Desktop/hotelapp2309/HotelApp2309/csvfiles/TA_restaurants_curated.csv"
rating_treshold = 4.0
city_counts = restaurantNumbers("/Users/jeroenhadderingh/Desktop/hotelapp2309/HotelApp2309/csvfiles/TA_restaurants_curated.csv", rating_treshold)
print(f"Highly rated City Counts (rating > {rating_treshold}):")
print(city_counts)