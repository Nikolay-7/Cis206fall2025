import csv

with open('NorthwindCustomers.txt', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    customers = list(csv_reader)

# Display results
print(f"Total customers: {len(customers)}")
print(f"\nFirst customer: {customers[0]}")

