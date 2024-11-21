import csv
import time
import datetime
from functools import wraps
 
datetime.datetime.now()
log_format = "%(asctime)s:%(filename)s:%(lineno)s:%(message)s"
 
def csvf(func):
    @wraps(func)
    def inner(*args, **kwargs):
        date = time.strftime('logs\\%d_%m_%y')
        result = func(*args, **kwargs)
 
        with open(date+'.csv', 'a', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(result)
       
        return result
    return inner