import datetime
import time

# from datetime import datetime, timedelta

import pytz


# dt = datetime.today() - timedelta(1)
# start_date = dt.replace(hour=0, minute=0, second=0, microsecond=0)
# end_date = dt.replace(hour=23, minute=59, second=59, microsecond=0)


# dt = pytz.timezone("UTC").localize(dt)

# start_dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
# end_dt = dt.replace(hour=23, minute=59, second=59, microsecond=0)
# print(start_dt.tzinfo)
# print(start_date, end_date)

# c = "2022-11-11"

# q = "2022-08-03"
# c = datetime.datetime.strptime(q, "%Y-%m-%d").date()
# print(type(str(c)))
# dt = datetime.datetime.fromtimestamp(
#     int(time.time()),
#     pytz.timezone("America/New_York"),
# ),
# print(dt)
# print(int(time.time())*1000,)

# d = datetime.date.today()
# print(d)

# dt = pytz.timezone("UTC")
# print(type(dt))


# a = {"code": {}}
# a["code"]["v"] = 0
# print(a)

# a = False
# if a:
#     print(1)
# if not a:
#     print(2)
# if a is None:
#     print(3)

a = datetime.datetime(2022, 8, 9, 12, 17)
print(a.tzinfo) 
>>> None
