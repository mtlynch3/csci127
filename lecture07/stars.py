import pandas as pd

#store the CSV file as a DataFrame 
stars = pd.read_csv("stars.csv")

#Prints the luminosity of the brightest star.
print("Luminosity of brighest star:", stars['Luminosity(L/Lo)'].max())

#Prints the temperature of the coldest star.
print("Temperature of coldest star:", stars['Temperature(K)'].min())

#Prints the average radius of a Hypergiant.
grouped = stars.groupby('Star type')
hypergiant = grouped.get_group('Hypergiant')

print("Hypergiant average radius:", hypergiant['Radius(R/Ro)'].mean())

#same as above but all on one line
print(stars.groupby('Star type').get_group('Hypergiant')['Radius(R/Ro)'].mean())

