# Import the pandas and PyPDF2 packages
import pandas as pd
import PyPDF2

# Open the PDF file
with open('example.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    reader = PyPDF2.PdfFileReader(pdf_file)

    # Create an empty DataFrame
    df = pd.DataFrame()

    # Iterate over the pages of the PDF
    for page_num in range(reader.numPages):
        #print out the page number

        # Get the current page
        page = reader.getPage(page_num)

        # Extract the text from the page
        text = page.extractText()
        print(text)

        # append the text using pandas.concat()
        df = pd.concat([df, pd.DataFrame([text])])

    # Print the DataFrame
    print(df)
