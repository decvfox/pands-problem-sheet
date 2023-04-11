# Bank.py
# Reads in 2 amounts, adds them, and then prints the answer
# author Declan Fox
# ref https://realpython.com/python-f-strings/

# The next 2 lines assigns as an integer the values entered by the user to amount1 and amount2.
amount1 = int(input("Enter amount1 in cents: "))
amount2 = int(input("Enter amount2 in cents: "))

# sum is assigned the value of the 2 amounts added together
sum = amount1 + amount2

euros = sum // 100 # calculates the amount of euros
cents = sum % 100 # calculates the amount of cents

# Formats and prints out the euro amount
print(f'The sum of these is €{euros}.{cents}')
