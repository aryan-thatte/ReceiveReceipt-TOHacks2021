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
		continue
	
	elif(name == 'q'):
		break
		
table.add_row(['TOTAL', total])
print(table)
print('\nThanks for shopping with us :)')
print('Your total bill amount is ', total, '/-')


table_txt = table.get_string()
with open('receipt.csv', 'w') as file:
    file.write(table_txt)


receiver = input("Email: ")
body = "Attatched is your receipt"
filename = input("File Name: receipt.csv")

yag = yagmail.SMTP('ReceiverReceipt@gmail.com', 'aryansahirelysia123')
yag.send(
    to=receiver,
    subject="Your Receipt",
    contents=body, 
    attachments=filename,
)
