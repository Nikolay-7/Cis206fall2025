import csv

with open('Northwind.txt', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  #skips header
    customers = list(csv_reader)

def show_menu():
    print("\n1. Display customers sorted by company name")
    print("2. Display customers sorted by contact name")
    print("3. Search customers by company name")
    print("4. Search customers by contact name")
    print("5. Exit")

def display_by_company():
    for c in sorted(customers, key=lambda x: x[1]):
        print(f"Company: {c[1]}, Contact: {c[2]}, Phone: {c[9]}")

def display_by_contact():
    for c in sorted(customers, key=lambda x: x[2]):
        print(f"Contact: {c[2]}, Company: {c[1]}, Phone: {c[9]}")

def search_company():
    name = input("Enter company name to search: ").lower()
    for c in customers:
        if name in c[1].lower():
            print(f"\nCustomerID: {c[0]}\nCompany: {c[1]}\nContact: {c[2]}\nTitle: {c[3]}\nPhone: {c[9]}\n")

def search_contact():
    name = input("Enter contact name to search: ").lower()
    for c in customers:
        if name in c[2].lower():
            print(f"\nCustomerID: {c[0]}\nCompany: {c[1]}\nContact: {c[2]}\nTitle: {c[3]}\nPhone: {c[9]}\n")

while True:
    show_menu()
    choice = input("\nEnter choice: ")
    
    if choice == '1':
        display_by_company()
    elif choice == '2':
        display_by_contact()
    elif choice == '3':
        search_company()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
