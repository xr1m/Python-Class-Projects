# Current date and time:

from datetime import datetime, date, time

today = date.today()
current = datetime.now()

print(f"Today's date is: {today} and current time is: {current}")

print("Date Component:", today.day, today.month, today.year)

import calendar

userinput = int(input("Enter for which year you want to display the calendar: "))
month = int(input("Enter the desired month to be displayed: "))
print(calendar.month(userinput, month))
print(calendar.calendar(userinput))