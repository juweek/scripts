import csv
from us import states

# Open the input and output CSV files
with open('cities.csv') as input_file, open('counties.csv', 'w') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Write the header row to the output CSV
    writer.writerow(['City', 'State', 'County'])

    # Skip the header row of the input CSV
    next(reader)

    # Iterate over the rows in the input CSV
    for city, state in reader:
        # Look up the state object for the given state
        state_obj = states.lookup(state)

        # Write the city, state, and county to the output CSV
        writer.writerow([city, state, state_obj.counties[city]])
