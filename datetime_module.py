import datetime
current_date_time=datetime.datetime.now()
print("current date time is",current_date_time)

#To change the format we strftime()
print(current_date_time.strftime("%d/%m/%Y %H:%M:%S"))

print(current_date_time.strftime("%d/%b/%Y %H:%M:%S"))


#to check the version of python

import sys
print("Python version is this: ",sys.version)


