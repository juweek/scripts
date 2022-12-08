import csv
from us import states
import requests
import json

# Create a dictionary mapping state abbreviations to state names
ap_to_name = {
    "Ala.": "Alabama",
    "Alaska": "Alaska",
    "Ariz.": "Arizona",
    "Ark.": "Arkansas",
    "Calif.": "California",
    "Colo.": "Colorado",
    "Conn.": "Connecticut",
    "Del.": "Delaware",
    "D.C.": "District of Columbia",
    "Fla.": "Florida",
    "Ga.": "Georgia",
    "Hawaii": "Hawaii",
    "Idaho": "Idaho",
    "Ill.": "Illinois",
    "Ind.": "Indiana",
    "Iowa": "Iowa",
    "Kan.": "Kansas",
    "Ky.": "Kentucky",
    "La.": "Louisiana",
    "Md.": "Maryland",
    "Maine": "Maine",
    "Mass.": "Massachusetts",
    "Mich.": "Michigan",
    "Minn.": "Minnesota",
    "Miss.": "Mississippi",
    "Mo.": "Missouri",
    "Mont.": "Montana",
    "Neb.": "Nebraska",
    "Nev.": "Nevada",
    "N.H.": "New Hampshire",
    "N.J.": "New Jersey",
    "N.M.": "New Mexico",
    "N.Y.": "New York",
    "N.C.": "North Carolina",
    "N.D.": "North Dakota",
    "Ohio": "Ohio",
    "Okla.": "Oklahoma",
    "Ore.": "Oregon",
    "Pa.": "Pennsylvania",
    "R.I.": "Rhode Island",
    "S.C.": "South Carolina",
    "S.D.": "South Dakota",
    "Tenn.": "Tennessee",
    "Texas": "Texas",
    "Utah": "Utah",
    "Vt.": "Vermont",
    "Va.": "Virginia",
    "Wash.": "Washington",
    "W.Va.": "West Virginia",
    "Wis.": "Wisconsin",
    "Wyo.": "Wyoming"
}

# Read the CSV file and store the rows in a list
with open('clean_data.csv') as csvfile:
    reader = csv.reader(csvfile)

    next(reader)
    rows = [row for row in reader]
    print(len(rows))

# Iterate over the rows in the list after skipping the header row and look up the FIPS code or county for each city
for row in rows:

    city = row[3]

    state_abbr = row[4]
    state_name = ap_to_name[state_abbr]
    print('/////////')
    print(rows.index(row))
    print(city + ', ' + state_name)
    # remove spaces from the city name if there is a space at the end
    if (city[-1] == ' '):
        city = city[:-1]

    # Look up the FIPS code for the city
    # The Census Bureau's API requires the state name to be spelled out
    # The API also requires the city name to be in all caps
    # The API also requires the city name to be separated by a plus sign if it contains a space
    #
    # #call the API
    url = 'https://api.census.gov/data/2017/acs/acs5?get=NAME,GEO_ID&for=place:*&in=state:{}&key='.format(
        states.lookup(state_name).fips, city.upper().replace(' ', '+'))
    response = requests.get(url)
    data = json.loads(response.text)
    # find the city in the response and print the FIPS code
    for place in data:
        currentCityName = place[0].split(',')[0]
        if (currentCityName == 'NAME'):
            continue

        # remove the last word in the currentCityName string
        currentCityName = currentCityName.split(' ')
        currentCityName.pop()
        currentCityName = ' '.join(currentCityName)
        if (city in currentCityName):
            #print('found the city')
            #print('this is the city that has the data:' + currentCityName)
            #print('this is the city you want the data from : ' + city)
            #print('this is the fips code: ' + place[2])
            # print(place)
            # print('=======')
            geoID = place[1]
            fips = place[1].split('US')[1]
            # drop the last two digits of the fips code
            print(geoID)
            fips = fips[:-2]
            # Extract the state and place codes from the GEOID
            state_fips = geoID[9:11]
            place_code = geoID[9:]

            # Use the `us` library to look up the state and place based on their codes
            print(state_fips)
            state_code = states.lookup(state_name).fips
            print(state_code)
            print(states.lookup(state_fips))

            place_code = "0455000"  # This is the place code for the city of Birmingham, Alabama
            # Call the Census Bureau's API to get the county's FIPS code
            url = 'https://api.census.gov/data/2017/acs/acs5?get=NAME,GEO_ID&for=place:*&in=state:{}&key='.format(
                state_code)
            response = requests.get(url)
            data = json.loads(response.text)
            for place in data:
                geoID = place[1]
                fips = geoID.split('US')

            # row.append(fips)
            break
        # check if the current city name is somewhere in the first string of the place list

# Write the updated rows to a new CSV file
with open('cities_with_fips.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
        writer.writerow(row)
