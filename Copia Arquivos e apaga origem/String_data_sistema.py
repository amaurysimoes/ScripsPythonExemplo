from datetime import datetime
from dateutil.parser import parse

#Defining format...
datetime_in_string = "31/12/2000 - 23:59:59"
 
#Converting string to datetime...
result2 = parse(datetime_in_string)
print(result2)