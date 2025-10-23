#imports northwind customers
import csv

def read_customers(filename):
    #reads customers file
    #returns list of records
    try:
        with open(filename, 'r',  encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            return list(csv_reader)
    except FileNotFoundError:
        return []

def show_menu():
    #display's options
    print('\n1. Display customers sorted by company name')
    print('2. Display customers sorted by contact name')
    print('3. Search customers by company name')
    print('4. Search customers by contact name')
    print('5. Exit')

def sort_display(customers, field_idx, format_type):
    #sorts and display's customers by field
    for c in sorted(customers, key=lambda x: x[field_idx]):
        if format_type == 'company':
            print(f'Company: {c[1]}, Contact: {c[2]}, Phone: {c[9]}')
        else:
            print(f'Contact: {c[2]}, Company: {c[1]}, Phone: {c[9]}')

def search_display(customers, field_idx):
    #searches and display's customer records
    term = input('Enter name to search: ').strip()
    if not term:
        return
    results = [c for c in customers if term.lower() in c[field_idx].lower()]
    if not results:
        print('No matches')
    for c in results:
        print(f'\nCustomerID: {c[0]}\nCompany: {c[1]}\nContact: {c[2]}\nTitle: {c[3]}\nPhone: {c[9]}')

def main():
    #program loop
    customers = read_customers('Northwind.txt')
    if not customers:
        print('No data loaded')
        return
    
    while True:
        show_menu()
        choice = input('\nEnter choice:').strip()
        
        if choice == '1':
            sort_display(customers, 1, 'company')
        elif choice == '2':
            sort_display(customers, 2, 'contact')
        elif choice == '3':
            search_display(customers, 1)
        elif choice == '4':
            search_display(customers, 2)
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()


   