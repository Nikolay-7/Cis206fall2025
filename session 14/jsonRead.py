import json

#loads and display's JSON book file
with open('BooksJson.py', 'r') as f:
    data = json.load(f)
    #display's books in JSON file
print("All Books in Library:")
for book in data['books']:
    print(f"{book['title']} by {book['author']} ({book['year']})")

print("\n" + "-"*50 + "\n")

#loop to prompt for book title
while True:
    search = input("Enter book title (or 'q' to exit): ")
    
    if search.lower() == 'q':
        break
    
    found = False
    for book in data['books']:
        if book['title'].lower() == search.lower():
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year: {book['year']}")
            found = True
            break
    
    if not found:
        print(f"'{search}' - title not found")
    
    print()
