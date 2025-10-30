import csv

with open('NorthwindCustomers.txt', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    customers = list(csv_reader)

def show_menu():
    print('\n1. Display customers sorted by company name')
    print('2. Display customers sorted by contact name')
    print('3. Search customers by company name')
    print('4. Search customers by contact name')
    print('5. Exit')

def display_by_company():
    for c in sorted(customers, key=lambda x: x['CompanyName']):
        print(f'Company: {c["CompanyName"]}, Contact: {c["ContactName"]}, Phone: {c["Phone"]}')

def display_by_contact():
    for c in sorted(customers, key=lambda x: x['ContactName']):
        print(f'Contact: {c["ContactName"]}, Company: {c["CompanyName"]}, Phone: {c["Phone"]}')

def search_company():
    name = input('Enter company name to search: ').lower()
    for c in customers:
        if name in c['CompanyName'].lower():
            print(f'\nCustomerID: {c["CustomerID"]}\nCompany: {c["CompanyName"]}\nContact: {c["ContactName"]}\nTitle: {c["ContactTitle"]}\nPhone: {c["Phone"]}\n')

def search_contact():
    name = input('Enter contact name to search: ').lower()
    for c in customers:
        if name in c['ContactName'].lower():
            print(f'\nCustomerID: {c["CustomerID"]}\nCompany: {c["CompanyName"]}\nContact: {c["ContactName"]}\nTitle: {c["ContactTitle"]}\nPhone: {c["Phone"]}\n')

while True:
    show_menu()
    choice = input('\nEnter choice: ')
    
    if choice == '1':
        display_by_company()
    elif choice == '2':
        display_by_contact()
    elif choice == '3':
        search_company()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        print('Goodbye!')
        break
    else:
        print('Invalid choice!')
