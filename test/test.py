from sqlite3 import Timestamp
import pandas as pd
from datetime import datetime

# a = pd.to_datetime(datetime.now())
# print(a
# )
# print(type(a))


time_delta = datetime.now() - datetime(2015, 12, 12, 3, 3, 3)
print(time_delta)
period_condition = "day" if time_delta.days < 365 else\
                   "week" if time_delta.days <= 1825 else\
                   "month"

print(period_condition)