from sqlalchemy import create_engine, text
import os

# Load database URL
DATABASE_URL = "postgresql://postgres:poop@localhost/bookdb"
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

# Connect to PostgreSQL
engine = create_engine(DATABASE_URL)
conn = engine.connect()

#sql commands
create_user_talbe = text("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO users
    (username, password)
    VALUES ('nick','poop');
""")

create_book_talbe = text("""
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    isbn TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL
);
""")

delete_tables = text("""
DROP TABLE IF EXISTS books, users;
""")

fill_book_table = text("""

""")

# optional deletion and re-initializatoin
yesno = input("type 1 to delete all tables and re-initialize them ")
if yesno == "1":
    print("deleting them")
    with engine.begin() as conn:
        conn.execute(delete_tables)
        conn.execute(create_book_talbe)
        conn.execute(create_user_talbe)
    print("tables remade.")

#fill books from csv
#with engine.begin() as conn:
#    conn.execute(fill_book_table)


#end
conn.close()
print('done')