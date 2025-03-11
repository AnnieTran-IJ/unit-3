import sqlite3

con = sqlite3.connect('sugarbliss_database.db')
cursor = con.cursor()
# Create the order table
order_table = """   
    CREATE TABLE IF NOT EXISTS order_table (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,  
    customer_name TEXT,         
    product_list TEXT,
    total_price INTEGER
);
"""
cursor.execute(order_table)

customer_database = """   
    CREATE TABLE IF NOT EXISTS customer_database (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    phone_number INTEGER NOT NULL,
    address TEXT NOT NULL
);
"""
cursor.execute(customer_database)

admin_dashboard = """   
    CREATE TABLE IF NOT EXISTS admin_dashboard (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    progress TEXT default 'Order Received',
    customer_name TEXT,
    order_list TEXT,
    total_payment INTEGER,
    profit INTEGER
);
"""
cursor.execute(admin_dashboard)

# cursor.execute("DROP TABLE admin_dashboard;")
# cursor.execute("DROP TABLE customer_database;")
# cursor.execute("DROP TABLE order_table;")

# Commit changes
con.commit()

