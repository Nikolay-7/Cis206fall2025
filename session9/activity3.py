import csv

def read_customers(filename):
    # reads customers from information
    # returns list of dictionaries
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []

def show_menu():
    # menu options
    print('\n1. Display customers sorted by company name')
    print('2. Display customers sorted by contact name')
    print('3. Search customers by company name')
    print('4. Search customers by contact name')
    print('5. Exit')

def sort_display(customers, key, fmt):
    #sorts and display's customers info
    for c in sorted(customers, key=lambda x: x[key]):
        if fmt == 'company':
            print(f'Company: {c["CompanyName"]}, Contact: {c["ContactName"]}, Phone: {c["Phone"]}')
        else:
            print(f'Contact: {c["ContactName"]}, Company: {c["CompanyName"]}, Phone: {c["Phone"]}')

def search_display(customers, key):
    #searches and shows records of company or contact name
    term = input('Enter name to search: ').strip()
    if not term:
        return
    results = [c for c in customers if term.lower() in c[key].lower()]
    if not results:
        print('No matches found.')
    for c in results:
        print(f'\nCustomerID: {c["CustomerID"]}\nCompany: {c["CompanyName"]}\nContact: {c["ContactName"]}\nTitle: {c["ContactTitle"]}\nPhone: {c["Phone"]}')

def main():
    #loop to keep asking for customer search
    customers = read_customers('NorthwindCustomers.txt')
    if not customers:
        print('No data loaded.')
        return
    
    while True:
        show_menu()
        choice = input('\nEnter choice: ').strip()
        
        if choice == '1':
            sort_display(customers, 'CompanyName', 'company')
        elif choice == '2':
            sort_display(customers, 'ContactName', 'contact')
        elif choice == '3':
            search_display(customers, 'CompanyName')
        elif choice == '4':
            search_display(customers, 'ContactName')
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice!')

if __name__ == '__main__':
    main()
