import datetime
import time


account_name = input("Enter your account name here: ")
beneficiary_acct_no = input("Enter your account number here: ")
phone_number = input("Enter your phone number here: ")
depositor_name = input("Enter depositor's name here: ")
terminal_id = '27012351'
branch = 'YABA BRANCH'
transaction_no = '003030'
deposit_time = str(datetime.datetime.now().time())
transaction_status = 'SUCCESSFUL'


note = int(input("Enter denomination: "))
count = int(input("Enter number of note: "))
amount = note * count
total = amount
print()

print("Hi, Welcome to Firstbank")
print('     Transaction Receipt'.upper())
print('Account Name: ' + account_name)
print('Terminal ID: ' + terminal_id)
print('Branch: ' + branch)
print('Beneficiary Account Number: ' + beneficiary_acct_no)
print('Phone Number: ' + phone_number)
print("Depositor's Name: " + depositor_name)
print('Transaction No: ' + transaction_no)
print('Deposit Time: ' + deposit_time)
print('Transaction Status: ' + transaction_status)
print('NOTE: ', '$', note)
print('Count: ', count)
print('Amount: ', '$', amount)
print("Thank you for banking with us!")
