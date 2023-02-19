# accounts.py
# Replaces all but the last 4 digits in an account number of any length with Xs
# ref https://www.w3schools.com/python/python_strings_slicing.asp
#for 10 digit version see: https://github.com/decvfox/mywork/blob/main/week03/lab3.3.4-accounts.py
# Author: Declan Fox

hidden_numbers = ''
account_number = input("Please enter an account number: ")
visible_numbers = account_number[(len(account_number)- 4):len(account_number)] 

for i in range(0, (len(account_number)- 4)):
    hidden_numbers += 'X'
print(hidden_numbers + visible_numbers)
