from datetime import date,time, datetime
today = date.today()
now = datetime.now()
print("Today's date:", today)
print("Current datetime:", now)
print("n/Current component of date and time:", today.day, today.month, today.year)