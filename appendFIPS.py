import pandas as pd
from us import states
from uscounties import Search

# Read the input CSV file into a DataFrame
df = pd.read_csv('counties.csv')

# Use the uscounties package to search for the county
def get_fips(row):
    state_obj = states.lookup(row.State)
    search = Search(state=state_obj.abbr, county=row.County)
    return search.results[0].fips

# Add a new column to the DataFrame with the county's FIPS code
df['FIPS'] = df.apply(get_fips, axis=1)

# Write the DataFrame to a new CSV file
df.to_csv('counties_fips.csv', index=False)
