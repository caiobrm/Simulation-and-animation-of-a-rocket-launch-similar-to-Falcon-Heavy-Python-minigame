import csv
import time
import datetime
from functools import wraps
 
datetime.datetime.now()
log_format = "%(asctime)s:%(filename)s:%(lineno)s:%(message)s"
 
 
#
#
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
 
# @csvf
# def test():task
#     a = 1 + 2
#     return a, a+1, a+2
 
 
# if __name__ == "__main__":
#     with open('csv_test.csv', 'w', newline='') as writeFile:
#         writer = csv.writer(writeFile)
#         writer.writerow(['nSensor', 'sensorData', 'date'])
 
#     for i in range (10):
#         test()