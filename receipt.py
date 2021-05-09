from prettytable import PrettyTable
from decimal import Decimal
from datetime import datetime
import yagmail
import psycopg

conn = psycopg.connect("defaultdb-test user-postgres")
cur =conn.cursor()
cur.execute("SELECT * FROM items")
records = cur.fetchall()


receiver = input("Email: ")

print('--------------WELCOME TO Walmart--------------\n')
table = PrettyTable(['Item Name', 'Item Price'])
total = 0

while(1):
    name = input('Enter Item name:')

    # 'q' to exit and print the table
    if(name != 'q'):
        price = Decimal(input('Enter the Price:'))

        # store all the prices in 'total'
        total += price
        table.add_row([name, price])
        with conn.cursor() as cur:
            cur.execute(
                'INSERT INTO items (id, first_name, email, item, price) VALUES name, price')
        conn.commit()
        continue

    elif(name == 'q'):
        break

table.add_row(['TOTAL', total])
print(table)
print('\nThanks for shopping with us :)')
print('Your total bill amount is', total)


table_txt = table.get_string()
with open('receipt.csv', 'w') as file:
    file.write(table_txt)

table_text = table.get_string()
with open('receipt.txt', 'w') as file:
    file.write(table_text)

body = "Attatched is your receipt"
filename = "receipt.txt"

yag = yagmail.SMTP('receivereceipt', 'aryansahirelysia123')
yag.send(
    to=receiver,
    subject="Your Receipt",
    contents=body,
    attachments=filename,
)


