# Bank.py
# Reads in 2 amounts, adds them, and then prints the answer
# author Declan Fox
# ref https://realpython.com/python-f-strings/

# The next 2 lines assigns as an integer the values entered by the user to amount1 and amount2.
amount1 = int(input("Enter amount1 in cents: "))
amount2 = int(input("Enter amount2 in cents: "))

# sum is assigned the value of the 2 amounts added together
sum = amount1 + amount2

# Formats and prints out the euro amount, sum / 100 returns a float
print(f'The sum of these is €{(sum / 100)}')
