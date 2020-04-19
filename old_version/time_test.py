import datetime
from datetime import timedelta
import time

st = datetime.date(2020, 3, 1)
#st = '2020-03-01'
et = datetime.date(2020, 4, 15)
day = timedelta(days=1)
print(et-st)
for i in range((et-st).days):
    print(st + i*day)
    print(st.day)
    time.sleep(2)