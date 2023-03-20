# square_root.py
# Create my own square root function using the newton method
# Works by starting off at the squared number itself and reducing it until 
# it reaches an approx of the root. 
# because r and r/x are averaged we could 
# start at 1 and get nearly the same results.
# for how it works visit:
# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# for a good explaination of why it works visit:
# https://math.stackexchange.com/questions/350740/why-does-newtons-method-work
#Author: Declan Fox

def sqrt(x):
    '''Calculates a square root'''
    # r = our "guess", x = the number we want to find the square root of.
    r = x # our first "quess" is x 
    precision = 10 ** (-10)  # precise to 10 decimal places

    while abs(x - r * r) > precision:
    # Our new guess is (x divided by our old guess) + our old guess all divided by 2
        r = (r + x / r) / 2 
    return r

num = float(input('Please enter a positive number: '))

print(f'The square root of {num} is approx. {sqrt(num)}')
