import random
import time
def getRandomDate(start_date, end_date):
    print("Printing a random date between", start_date, "and", end_date)
    randomgenerator = random.random()
    dateformat = "%Y-%m-%d"
    start_time = time.mktime(time.strptime(start_date, dateformat))
    end_time = time.mktime(time.strptime(end_date, dateformat))
    random_time = start_time + randomgenerator * (end_time - start_time)
    random_date = time.strftime(dateformat, time.localtime(random_time))
    return random_date
print(getRandomDate("2000-12-31", "2026-12-31"))