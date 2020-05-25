# Date and time
 Use the import statement to get date and time information
  ```python
       from datetime import date
       from datetime import time
       from datetime import datetime
   ```

## There are methods you can use to grab different parts of the date. 
```python
today()  #you can get today’s date
.day, .month, .year  #will then grab different components from the date
.weekday()  #you get today’s weekday number (0=Monday thru 6=Sunday)
``` 
### You can also get the date from the datetime class
```python 
today = datetime.now() 
```
### You can get the time from the datetime class
```python 
time = datetime.time(datetime.now())
```

### Formatting Date and Time
Using the .strftime() method and predefined strings we can print out formatted datetime components
```python	
%y/%Y - Year, 
%a/%A - weekday, 
%b/%B - month, 
%d - day of month 
```
Similarly with the time, we can use predefined strings to output formatted time components
```python
%I/%H - 12/24 Hour, 
%M - minute, 
%S - second, 
%p - locale AM/PM
```
For local information we can also use predefined strings
```python 
%c - locales date and time, 
%x - locales date, 
%X - locales time
```

### Example 
```python
from datetime import datetime
now = datetime.now()
print(now.strftime("%a, %d, %B, %y"))
print(now.strftime("Locale date and time: %c"))
print(now.strftime("the current time is: %I:%M:%S %p"))
```

## Using timedelta objects
Use import statement to work with timedelta objects
```python
from datetime import timedelta
```
A basic timedelta statement
```python
print(timedelta(days=365, hours=5, minutes=1))
```
Days, hours and minutes are all named parameters. 
   We can find dates in the future 
```python
print ("one year from now it will be " + str(now+timedelta(days=365)))
```
Or with two arguments
```python
print("In 2 days and 3 weeks, it will be " +
     str(now+timedelta(days=2, weeks=3)))
```
We can find dates in the past 
```python
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print ("one week ago it was " + s )
```

Or find out how long until a certain day 
### Example 
```python
	### How many days until April Fools' Day?

today = date.today() # today's date
afd = date(today.year, 4, 1) ## construct a new date that represents April fools day

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("April fools day was %d days ago" % ((today-afd).days))
    afd = afd.replace(year=today.year+1)

# Now calculate the amount of time until April Fool's Day 
time_to_afd = afd - today
print ("it's just ", time_to_afd.days, " days until april fools day")
```

# Calendars

## import the calendar module
```python
import calendar
```

## create a plain text calendar
```python
c = calendar.TextCalendar(calendar.SUNDAY)
 st = c.formatmonth(2017, 1, 0, 0)
 print(st)
```
## create an HTML formatted calendar
```python
 hc = calendar.HTMLCalendar(calendar.SUNDAY)
 st = hc.formatmonth(2017, 1, 0,)
 print(st)
``` 

## loop over the days of a month
### zeroes mean that the day of the week is in an overlapping month
```python 
 for i in c.itermonthdays(2017, 8):
     print (i)
```

  
## Locale
 The Calendar module provides useful utilities for the given locale,
such as the names of days and months in both full and abbreviated forms
```python
 for name in calendar.month_name:
     print(name)

 for day in calendar.day_name:
     print(day)
```

# Calculate days based on a rule 
For example, consider a team meeting on the first Friday of every month.
We need to figure out what days that would be for each month
```python 
print ("Team meetings will be on: ")
for m in range(1,13):
    cal = calendar.monthcalendar(2018, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    print ("%10s %2d" % (calendar.month_name[m], meetday))
```