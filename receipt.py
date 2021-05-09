from prettytable import PrettyTable
from decimal import Decimal
from datetime import datetime
import yagmail


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
            cur.execute('INSERT INTO ')
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

receiver = input("Email: ")
body = "Attatched is your receipt"
filename = "receipt.txt"

yag = yagmail.SMTP('receivereceipt', 'aryansahirelysia123')
yag.send(
    to=receiver,
    subject="Your Receipt",
    contents=body, 
    attachments=filename,
)






cockpw=cockroach sql --url 'postgres://eas:RXGxHKVrTFD17Fpa@free-tier5.gcp-europe-west1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=<your_certs_directory>/cc-ca.crt&options=--cluster=quirky-elk-300'

download CRDB :::  curl https://binaries.cockroachdb.com/cockroach-v20.2.8.darwin-10.9-amd64.tgz | tar -xJ; cp -i cockroach-v20.2.8.darwin-10.9-amd64/cockroach /usr/local/bin/

cockroach sql --url='postgres://eas:RXGxHKVrTFD17Fpa@free-tier5.gcp-europe-west1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=/Users/sahirbandali/certs/cc-ca.crt'