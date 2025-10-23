import csv

with open('Northwind.txt', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  #skips header
    customers = list(csv_reader)

#displays results
print(f"Total customers: {len(customers)}")
print(f"\nFirst customer: {customers[0]}")
