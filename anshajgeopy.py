import pandas
from geopy.geocoders import Nominatim

df = pandas.read_csv("supermarkets.csv")
print(df)
df["Address"]=df["Address"]+","+df["City"]+","+df["State"]
print(df.Address)
df["Coordinates"] = df["Address"].apply(Nominatim.geocode)
print(df)
