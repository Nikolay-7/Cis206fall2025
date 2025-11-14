import sqlite3

conn = sqlite3.connect("Northwind.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_list = [t[0] for t in cursor.fetchall()]

print("Tables:")
for i, name in enumerate(table_list):
    print(f"{i}. {name}")

table = table_list[int(input("Pick table #: "))]

cursor.execute(f"SELECT * FROM {table}")
data = cursor.fetchall()
col_names = [c[0] for c in cursor.description]

print("\n", " | ".join(col_names))
for i, row in enumerate(data):
    print(i, row)

if table in ["Customers", "Employees", "Products"]:
    action = input("\nI = insert, U = update, D = delete: ").upper()

    if action == "I":
        vals = [input(f"{c}: ") for c in col_names] 
        columns = ", ".join(col_names)  
        placeholders = ", ".join(["?"] * len(vals))
        cursor.execute(f"INSERT INTO {table}({columns}) VALUES ({placeholders})", vals)


    elif action == "U":
        row_num = int(input("Row #: ")) - 1  
        col_to_edit = input(f"Column to change {col_names}: ")
        new_value = input("New value: ")
        id_col = col_names[0]
        cursor.execute(
        f"UPDATE {table} SET {col_to_edit}=? WHERE {id_col}=?",
        (new_value, data[row_num][0])
        )

    elif action == "D":
        row_num = int(input("Row #: ")) - 1  
        id_col = col_names[0]
        cursor.execute(
        f"DELETE FROM {table} WHERE {id_col}=?",
        (data[row_num][0],)
        )


conn.commit()
conn.close()


