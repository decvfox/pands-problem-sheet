# pands-problem-sheet

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

[Datetime](https://docs.python.org/3/library/datetime.html) and 
[Time](https://docs.python.org/3/library/time.html?highlight=time#module-time) information on usage at docs.python.org

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

