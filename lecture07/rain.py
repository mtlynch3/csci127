#Import libraries.
import pandas as pd

#Read in the csv file.
rain = pd.read_csv('AustraliaRain.csv')

#Group the data by location
groupedData = rain.groupby('Location')

#Print the average rainfall for all locations
print(groupedData['Rainfall'].mean())

#Group the data by location but look specifically at group 'Albury' (one of the repeated values in the 'Location' column).
albury = rain.groupby('Location').get_group('Albury')

#Print the average rainfall for Albury.
print("Albury:", albury['Rainfall'].mean())