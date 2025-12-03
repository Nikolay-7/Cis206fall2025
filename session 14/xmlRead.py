import xml.etree.ElementTree as ET

#loads and display's XML book file
tree = ET.parse('BooksXml.py')
root = tree.getroot()

#display's books in XMl file
print("All Books in Library:")
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text
    print(f"{title} by {author} ({year})")

print("\n" + "-"*50 + "\n")

#loop to prompt for book title
while True:
    search = input("Enter book title (or 'q' to exit): ")
    
    if search.lower() == 'q':
        break
    
    #searches for the book
    found = False
    for book in root.findall('book'):
        title = book.find('title').text
        if title.lower() == search.lower():
            author = book.find('author').text
            year = book.find('year').text
            print(f"Title: {title}")
            print(f"Author: {author}")
            print(f"Year: {year}")
            found = True
            break
    
    if not found:
        print(f"'{search}' - title not found")
    
    print()
