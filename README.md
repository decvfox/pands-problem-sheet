# pands-problem-sheet

helloworld.py

Bank.py

accounts.py

collatz.py

    Demos the Collatz Conjecture

    Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation. 
    At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
    Have the program end if the current value is one.

    Example of it running:

    $ python collatz.py

    Please enter a positive integer: 10

    10 5 16 8 4 2 1

    Output requires formatting to print all numbers on the same line


### Weekly Task 05
#### weekday.py
Write a program that outputs whether or not today is a weekday.

E.G. for Thursday:
```
Yes, unfortunately today is a weekday.
```
For sunday:
```
It is the weekend, yay!
```

I used both the datetime and time modules in my code.

click [Datetime](https://docs.python.org/3/library/datetime.html) or 
[Time](https://docs.python.org/3/library/time.html?highlight=time#module-time) for usage information at docs.python.org

```python
time.strftime("%A")
```
Gets the name of the weekday(Sunday, Monday etc.).
```python
datetime.datetime.now()
```
Gets the current date and time. I used
```python
datetime.date.fromisoformat('2023-02-24')
```
for testing my code(e.g. for above, 24 was friday).
```python
date_time.isoweekday()
```
This returns the day of the week in number form where 1 is Monday, 2 is Tuesday and so on.

