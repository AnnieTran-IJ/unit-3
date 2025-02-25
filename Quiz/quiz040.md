# Quiz 040


## Flow Chart

### ER Diagram
![image](https://github.com/user-attachments/assets/dfafd2a2-a93f-43be-9d19-b02970f59171)

### UML Diagram
![image](https://github.com/user-attachments/assets/ed38faa2-da74-42f8-8965-62c3139ce24f)

## Code
```.py
import sqlite3

conn = sqlite3.connect('smallCase.db')

cursor = conn.cursor()

def detect_balance_discrepancies(cursor):
    discrepancies = []
    cursor.execute("""
        SELECT account_id, 
               (SELECT sum(amount) FROM transactions WHERE account_id = t.account_id AND transaction_type = 'deposit') -
               (SELECT sum(amount) FROM transactions WHERE account_id = t.account_id AND transaction_type = 'withdraw') AS calculated_balance
        FROM transactions t
        GROUP BY account_id
    """)
    calculated_balances = cursor.fetchall()
    cursor.execute("SELECT account_id, balance FROM accounts")
    stored_balances = {row[0]: row[1] for row in cursor.fetchall()}

    for account_id, calculated_balance in calculated_balances:
        stored_balance = stored_balances.get(account_id, 0)
        if calculated_balance != stored_balance:
            discrepancies.append({
                'account_id': account_id,
                'stored_balance': stored_balance,
                'calculated_balance': calculated_balance,
                'difference': calculated_balance - stored_balance
            })

    return discrepancies

balance_discrepancies = detect_balance_discrepancies(cursor)

if balance_discrepancies:
    print("Balance Discrepancies Detected:")
    for discrepancy in balance_discrepancies:
        cursor.execute("SELECT first_name, last_name, email FROM customers WHERE customer_id = (SELECT customer_id FROM accounts WHERE account_id = ?)", (discrepancy['account_id'],))
        customer = cursor.fetchone()
        print(f"Account ID: {discrepancy['account_id']}, "
              f"Customer: {customer[0]} {customer[1]} ({customer[2]}), "
              f"Stored Balance: ${discrepancy['stored_balance']}, "
              f"Calculated Balance: ${discrepancy['calculated_balance']}, "
              f"Difference: ${discrepancy['difference']}")
else:
    print("No balance discrepancies detected.")

conn.close()

```
## Proof of work
![image](https://github.com/user-attachments/assets/ad06bf1a-6a90-43ac-b7a5-d0ce009c6f79)
