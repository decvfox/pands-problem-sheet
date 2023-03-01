#  lab5.1.7-weekday.py
# Program that outputs whether or not today is a weekday
# ref https://docs.python.org/3/library/datetime.html
# ref https://docs.python.org/3/library/time.html?highlight=time#module-time
#Author: Declan Fox

import datetime, time

weekday = time.strftime("%A") # returns the day of the week.
date_time = datetime.datetime.now() # gets the current date and time.
weekday_number = date_time.isoweekday() # gets the day in number form, 1 = Monday up to 7 = Sunday

print(f'Today is {weekday}, day {weekday_number} of the week')

if weekday_number > 5:
    print('It is the weekend, yay!')
else:
    print('Yes, unfortunately today is a weekday.')         
    