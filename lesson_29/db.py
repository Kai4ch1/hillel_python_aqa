import psycopg2
from faker import Faker
from assertpy import assert_that, soft_assertions


fake_base = Faker()

def fake_author() -> str:
    return fake_base.first_name() + " " + fake_base.last_name()

def fake_book() -> str:
    return fake_base.color_name()

author = fake_author()
book = fake_book()

connection = psycopg2.connect(user="test_user",
                              password="test_pass",
                              host="db",
                              port="5432",
                              database="books_db")
cursor = connection.cursor()

cursor.execute(
            """CREATE TABLE IF NOT EXISTS books
               (
               id SERIAL PRIMARY KEY,
               name VARCHAR(255),
               author VARCHAR(255)
                    )
                    """)

# create
cursor.execute(f"INSERT INTO books (name, author) VALUES ('{book}', '{author}') RETURNING id;")
new_id = cursor.fetchone()[0]
connection.commit()

print(f"Book ID: {new_id}")

cursor.execute(f"SELECT * FROM books WHERE id = {new_id}")
last_record = cursor.fetchone()

with soft_assertions():
   assert_that(last_record[1]).is_equal_to(book)
   assert_that(last_record[2]).is_equal_to(author)
connection.commit()

# Update record

new_author = fake_author()
new_book = fake_book()
cursor.execute(
        f"""
        UPDATE books
        SET name='{new_book}', author='{new_author}'
        WHERE id = {new_id};
        """, )
connection.commit()

cursor.execute(f"SELECT * FROM books WHERE id = {new_id}")

updated_record = cursor.fetchone()
with soft_assertions():
    assert_that(updated_record[1]).is_equal_to(new_book)
    assert_that(updated_record[2]).is_equal_to(new_author)


print("Books updated=", updated_record[1], updated_record[2])
connection.commit()

# delete
cursor.execute(
        f"""
        DELETE FROM books
        WHERE id = {new_id}
        RETURNING id;
        """, )
deleted_record_id = cursor.fetchone()[0]
cursor.execute(f"SELECT * FROM books WHERE id = {deleted_record_id}")
deleted_record = cursor.fetchone()


with soft_assertions():
   assert_that(deleted_record).is_none()

print("Books deleted=", deleted_record_id, deleted_record)
connection.commit()



