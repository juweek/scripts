from bs4 import BeautifulSoup
import requests 

# Read the URL from the user
url = input("Enter a Wikipedia URL: ")

# Fetch the HTML of the page
response = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the tables on the page
tables = soup.find_all('table')

# Create a list to hold the data for each table
table_data = []

# Iterate over the tables and extract their data
for table in tables:
    # Create a dictionary to hold the data for this table
    table_info = {}

    # Extract the caption, if it exists
    caption = table.find('caption')
    if caption:
        table_info['caption'] = caption.text

    # Extract the headers
    headers = []
    header_row = table.find('thead')
    if header_row:
        for header in header_row.find_all('th'):
            headers.append(header.text)
    table_info['headers'] = headers

    # Extract the data
    rows = []
    body = table.find('tbody')
    if body:
        for row in body.find_all('tr'):
            cells = []
            for cell in row.find_all(['td', 'th']):
                cells.append(cell.text)
            rows.append(cells)
    table_info['rows'] = rows

    # Add the table's data to the list of tables
    table_data.append(table_info)

# Print the list of tables
print(table_data)
