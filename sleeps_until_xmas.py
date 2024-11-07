#Functions Challenge 5 – Sleeps until Christmas
#Write a function called sleeps_until_xmas that calculates how many days it is until Christmas and returns the number of sleeps left until the big day.

from datetime import datetime

def sleeps_until_xmas():
    today = datetime.today()
    xmas = datetime(2024, 12, 25)
    days_left = xmas - today
    return F"There are {days_left.days+1} 'sleeps' left until Christmas!"


print(sleeps_until_xmas())
 