import PyPDF2

# Open the PDF file
with open('c:\\!\\privat\\Buchungen\\KontoauszugTradeRepublikAndre.pdf', 'rb') as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)
    
    # Get the total number of pages in the PDF
    num_pages = len(reader.pages)
    print (num_pages)
    print(reader.pages[0].extract_text())