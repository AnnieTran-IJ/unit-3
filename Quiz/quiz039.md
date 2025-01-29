# Quiz 039

## Code
```.py
import sqlite3

haiku = """Code flows like a stream
Algorithms guide its way 
In silence, it solves
"""

database_name = "quiz039.db"
con = sqlite3.connect(database_name)
cursor = con.cursor()

#create database with table words
query_create_table = """
create table if not exists WORDS(
    id INTEGER PRIMARY KEY,
    length INTEGER,
    word TEXT UNIQUE

)
"""
cursor.execute(query_create_table)
con.commit()

for word in haiku.split():
    insert_query = "INSERT OR IGNORE INTO WORDS(length, word) VALUES (?, ?)"
    cursor.execute(insert_query, (len(word), word))
con.commit()

output = cursor.execute("SELECT AVG(length) FROM WORDS;")
average_length = output.fetchall()
print("Average word length is:", average_length)

con.close()
```
## Proof of work
![image](https://github.com/user-attachments/assets/0366f9f2-e262-4e5f-a40d-60c0f6c05dc0)

