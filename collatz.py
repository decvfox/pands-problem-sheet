# collatz.py
# Demos the Collatz Conjecture
#Author: Declan Fox

# Enter a positive integer and at each step through the loop
# calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, 
# multiply it by three and add one.
# end the program if the current value is one.


start_number = int(input("Please enter a positive integer: "))
print(start_number, end = ' ') # end = ' ' formats the output on the one line with spaces

while start_number > 1:
    if start_number % 2 == 0: # checks if even
        start_number //= 2 # // keeps results as integers
    else:
        start_number = (start_number * 3) + 1
    print(start_number, end = ' ') 
    