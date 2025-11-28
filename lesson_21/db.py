import sqlite3
from faker import Faker

db_name = "2. silpo-black-market.db"
table_products = "products"
table_categories = "categories"

db = sqlite3.connect(db_name)
cursor = db.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

CREATE_TABLE_CATEGORIES = f"""CREATE TABLE IF NOT EXISTS '{table_categories}'(
       category_id INTEGER PRIMARY KEY,
       category_name TEXT NOT NULL
 );
"""

CREATE_TABLE_PRODUCTS = f"""CREATE TABLE IF NOT EXISTS '{table_products}'(
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL UNIQUE,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories (category_id)
 );
 """
INSERT_CATEGORY = f"INSERT INTO CATEGORIES (category_name) VALUES ('delivered')"
INSERT_CATEGORY_2 = f"INSERT INTO CATEGORIES (category_name) VALUES ('pending')"

INSERT_PRODUCT = f"INSERT INTO PRODUCTS (product_name, category_id) VALUES ('{Faker().name()}', '1')"
INSERT_PRODUCT_2 = f"INSERT INTO PRODUCTS (product_name, category_id) VALUES ('{Faker().name()}', '2')"

JOIN = """
SELECT 
    p.product_name, 
    c.category_name
FROM products AS p
JOIN categories AS c 
    ON p.category_id = c.category_id;
"""

cursor.execute(JOIN)

result = cursor.fetchall()

for row in result:
    print(f"{row[0]} | {row[1]}")





