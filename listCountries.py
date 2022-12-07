import csv
import collections
import numpy as np
import matplotlib.pyplot as plt


#iterate over each row in file. on each row, store the country and the country's population. then, create a dictionary of countries and populations
with open('Data/world_population.csv') as file:
    reader = csv.reader(file)
    countries = []
    populations = []
    countryPopulationKey = {}

    #for each row, go into the file and get the race
    for row in reader:
        countries.append(row[0]);
        populations.append(row[2]);
        countryPopulationKey[row[0]] = row[2]

    ##the ability to out something print(countryPopulationKey);
    print(countryPopulationKey);





