import sqlite3

conn = sqlite3.connect("Northwind.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_list = [t[0] for t in cursor.fetchall()]

print("Tables:")
for i, name in enumerate(table_list):
    print(f"{i}. {name}")

table_num = int(input("Pick table #: "))
table = table_list[table_num]

cursor.execute(f"SELECT * FROM {table}")
data = cursor.fetchall()
cols = [c[0] for c in cursor.description]

print("\n", " | ".join(cols))
for i, row in enumerate(data, 1):
    print(i, row)

conn.close()
