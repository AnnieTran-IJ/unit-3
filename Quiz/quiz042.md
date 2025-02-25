# Quiz 042

## Flow Chart
### ER Diagram
![image](https://github.com/user-attachments/assets/faf15f53-f12b-4c73-8ba7-cc242a41dbf6)

## Code
```.py
from quiz.secure_password import encrypt_password
from secure_password import check_password
from my_lib import DatabaseManager

x = DatabaseManager('bitcoin_exchange.db')
result = x.search("SELECT * from ledger")
x.close()

for row in result:
    id, sender_id, receiver_id, amount, signature = row
    string_hash = f"id {id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}"
    if check_password(signature, string_hash):
        print("transaction is aligned")
    else: print("transaction is wrong")

```
## Proof of work
![image](https://github.com/user-attachments/assets/01992ef6-2351-4944-ae13-480974368ae8)
