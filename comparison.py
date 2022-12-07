#this will be an example of how we can show different data visualization formats using python's ggplot format

#first we will import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#now we will import the data
df = pd.read_csv('world_population.csv')

#now we will create a new column that will be the population in millions
#df['pop_millions'] = df['population']/1000000

#now we will iterate through all of the countries in the data set and print out the country name and the country population in 2020
for index, row in df.iterrows():
    print(row)
    #create a Dataframe using the row object
    df2 = pd.DataFrame(row)
    #print the dataframe
    print(df2)
    print(type(df2))
    print('=================')
    
    #now we will plot the data
    #first we will create a plot object using the dataframe
    plot = df2.plot(kind='bar')
    #now we will show the plot
    plt.show()


