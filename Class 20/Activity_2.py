# Random date and time:

import random
import time

def randomdate(startdate, enddate):
    print("Printing random date between:", startdate, "and", enddate)
    randomgenerator = random.random()
    dateformat = "%m/%d/%Y"
    starttime = time.mktime(time.strptime(startdate, dateformat))
    endtime = time.mktime(time.strptime(enddate, dateformat))
    randomtime = starttime + randomgenerator * (endtime - starttime)
    randomdate = time.strftime(dateformat, time.localtime(randomtime))
    return randomdate
print("Random date =", randomdate("1/1/2024", "1/1/2026"))