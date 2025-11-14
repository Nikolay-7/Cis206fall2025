import sqlite3

#opens northwind database
def open_db(name):
    return sqlite3.connect(name)

#gets a list of all tables in database
def list_tables(db):
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [t[0] for t in cursor.fetchall()]

#shows tables user selects
def show_table(db, table):
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    columns = [c[0] for c in cursor.description]
    print("\n", " | ".join(columns))
    for i, row in enumerate(rows, start=1):
        print(i, row)
    return rows, columns

#Inserts row data into database with validation
def insert_row(db, table, columns):
    cursor = db.cursor()
    values = []
    for col in columns:
        val = input(f"{col}: ").strip()
        if val == "":
            raise ValueError(f"{col} cannot be empty")
        if table == "Customers" and col == "CustomerID" and len(val) != 5:
            raise ValueError("CustomerID must be 5 characters")
        values.append(val)
    placeholders = ','.join(['?'] * len(values))
    cursor.execute(f"INSERT INTO {table}({','.join(columns)}) VALUES ({placeholders})", values)
    db.commit()
    print("Row inserted.")

#updates row data in database with validation
def update_row(db, table, rows, columns):
    row_num = int(input("Row #: ")) - 1  # user input starts at 1
    if row_num not in range(len(rows)):
        raise ValueError("Invalid row number")

    col_map = {c.lower(): c for c in columns}
    col_input = input(f"Column to update {columns}: ").strip().lower()
    if col_input not in col_map:
        raise ValueError("Invalid column")
    col_name = col_map[col_input]

    new_val = input("New value: ").strip()
    if new_val == "":
        raise ValueError("Value cannot be empty")

    cursor = db.cursor()
    cursor.execute(f"UPDATE {table} SET {col_name}=? WHERE {columns[0]}=?", (new_val, rows[row_num][0]))
    db.commit()
    print("Row updated.")

#delete row in database with validation
def delete_row(db, table, rows, columns):
    row_num = int(input("Row #: ")) - 1
    if row_num not in range(len(rows)):
        raise ValueError("Invalid row number")
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM {table} WHERE {columns[0]}=?", (rows[row_num][0],))
    db.commit()
    print("Row deleted.")

#runs all functions
def main():
    db = open_db("Northwind.db")
    tables = list_tables(db)
    print("Tables:")
    for i, t in enumerate(tables):
        print(i, t)

    table_choice = int(input("Table #: "))
    if table_choice not in range(len(tables)):
        raise ValueError("Invalid table selection")
    table = tables[table_choice]

    rows, columns = show_table(db, table)

    if table in ["Customers", "Employees", "Products"]:
        action = input("I=insert, U=update, D=delete: ").upper()
        if action == "I":
            insert_row(db, table, columns)
        elif action == "U":
            update_row(db, table, rows, columns)
        elif action == "D":
            delete_row(db, table, rows, columns)
        else:
            raise ValueError("Invalid action")

    db.close()

if __name__ == "__main__":
    main()


