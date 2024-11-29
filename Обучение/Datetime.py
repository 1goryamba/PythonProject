import datetime

yesterday = datetime.date(2024,11,29)
print(yesterday)

from datetime import date

today = date.today()
print(today)
print("{}.{}.{}".format(today.day, today.month, today.year))

from datetime import time

current_time = time()
print(current_time)

current_time = time(13)
print(current_time)

current_time = time(13, 20)
print(current_time)

from datetime import datetime

deadline = datetime(2024, 7, 13, 24, 15, 45)
print(deadline)

deadline = datetime (2024, 11, 29, 14, 30, 30)
print(deadline)

from datetime import datetime

now = datetime.now()
print(now)
print(now.date())
print(now.time())


from datetime import datetime

deadline = datetime.strptime("29/11/2024","%d/%m/%Y")
print(deadline)