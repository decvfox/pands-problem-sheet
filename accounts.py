# accounts.py
# Replaces all but the last 4 digits in an account number of any length with Xs
# ref https://www.w3schools.com/python/python_strings_slicing.asp
# For 10 digit only version see: 
# https://github.com/decvfox/mywork/blob/main/week03/lab3.3.4-accounts.py
# Author: Declan Fox

# creates an empty string variable 
hidden_numbers = ''

# account_number is assigned a string of any length that's entered by the user
account_number = input("Please enter an account number: ")

# visible_number is assigned the last 4 charachters of account_number
# len(account_number) gives us the length of the string
visible_numbers = account_number[(len(account_number)- 4):len(account_number)] 

# for loop will itterate until we reach the last 4 digits 
for i in range(0, (len(account_number)- 4)):
    hidden_numbers += 'X' # this line adds an X to hidden_numbers at each itteration

 # Joins the 2 strings and prints them   
print(hidden_numbers + visible_numbers)
