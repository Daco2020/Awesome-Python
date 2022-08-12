from pytz import BaseTzInfo
import pytz
from datetime import datetime, timedelta, timezone, tzinfo

# dt = datetime.now().replace(microsecond=0)
# a = dt.timestamp()
# print(int(a*1000))

# print(dt.time())
# print(type(dt.time()))


tz = pytz.timezone('America/New_York')
# cur_time = datetime.now(tz)
# simple_cur_time = cur_time.strftime("%H:%M:%S")
# print(f'NY time: {cur_time}')
# print(f'NY time: {simple_cur_time}')

# timestamp = 1659000988000
# dttime = datetime.fromtimestamp(timestamp/1000)
# print(dttime)
# dttime = datetime.fromtimestamp(timestamp/1000, tz=tz)
# print(dttime)
# a = datetime.now(tz=tz).replace(microsecond=0)
# b = dttime.date()
# c = a.date()
# a = datetime.today().astimezone(tz) - timedelta(1)
# e = datetime.today()
# print(a, e)
# f = a.tzinfo
# print(a.tzinfo)
# print(type(a.tzinfo))

# print(isinstance(f, str))
# print(isinstance(f, tzinfo))
# print(isinstance(pytz.timezone("UTC"), tzinfo))


# a = [
#     ("2022-08-08 20:00:00", "1", "2"),
#     ("2019-08-08 19:00:00", "open", "1"),
#     ("2025-08-08 17:50:00", "5", "close"),
#     ("2021-08-05 18:30:00", "2", "9"),
# ]


values = [{"datetime": "2022-08-10 23:00:00", "open": "1299.93005",
           "high": "1300.08496", "low": "1296.59497", "close": "1.81006"},
          {"datetime": "2022-08-10 22:00:00", "open": "1302.24500",
           "high": "1308.96997", "low": "1299.78503", "close": "1299.87000"},
          {"datetime": "2022-08-10 21:00:00", "open": "1311.01001",
           "high": "1311.89001", "low": "1298.52502", "close": "1302.24500"},
          {"datetime": "2022-08-10 20:00:00", "open": "1310.88000",
           "high": "1311.34998", "low": "1310.72998", "close": "1311.06006"},
          {"datetime": "2022-08-10 19:00:00", "open": "1309.98999",
           "high": "1311.03003", "low": "1309.97998", "close": "1310.91003"},
          {"datetime": "2022-08-10 18:00:00", "open": "1310.12500",
           "high": "1312.07495", "low": "1309.93005", "close": "1309.95996"},
          {"datetime": "2022-08-10 17:00:00", "open": "1312.01501",
           "high": "1312.88501", "low": "1310.08997", "close": "1310.30505"},
          {"datetime": "2022-08-10 16:00:00", "open": "1310.45996",
           "high": "1311.81995", "low": "1310.12000", "close": "1311.81995"},
          {"datetime": "2022-08-10 15:00:00", "open": "1310.34497",
           "high": "1311.37000", "low": "1310.30505", "close": "1310.46997"},
          {"datetime": "2022-08-10 14:00:00", "open": "1309.64001",
           "high": "1310.65002", "low": "1309.60999", "close": "1310.37000"},
          {"datetime": "2022-08-10 13:00:00", "open": "1308.51501",
           "high": "1309.98499", "low": "1308.46997", "close": "1309.52002"},
          {"datetime": "2022-08-10 12:00:00", "open": "1308.14001",
           "high": "1308.67004", "low": "1307.63501", "close": "1308.66003"},
          {"datetime": "2022-08-10 11:00:00", "open": "1307.59497",
           "high": "1308.71997", "low": "1307.45496", "close": "1308.12500"},
          {"datetime": "2022-08-10 10:00:00", "open": "1309.04504",
           "high": "1309.04504", "low": "1307.14502", "close": "1307.68994"},
          {"datetime": "2022-08-10 09:00:00", "open": "1307.85999",
           "high": "1309.55005", "low": "1306.59998", "close": "1309.04504"},
          {"datetime": "2022-08-10 08:00:00", "open": "1307.26001",
           "high": "1307.91003", "low": "1307.26001", "close": "1307.85999"},
          {"datetime": "2022-08-10 07:00:00", "open": "1307.26001",
           "high": "1307.28003", "low": "1307.25000", "close": "1307.26001"},
          {"datetime": "2022-08-10 06:00:00", "open": "1307.91003",
           "high": "1307.91003", "low": "1307.26001", "close": "1307.26001"},
          {"datetime": "2022-08-10 05:00:00", "open": "1307.92004",
           "high": "1308.21997", "low": "1307.64001", "close": "1307.72998"},
          {"datetime": "2022-08-10 04:00:00", "open": "1307.90002",
           "high": "1308.05005", "low": "1307.84998", "close": "1307.93994"},
          {"datetime": "2022-08-10 03:00:00", "open": "1307.66003",
           "high": "1307.96997", "low": "1307.39001", "close": "1307.96997"},
          {"datetime": "2022-08-10 02:00:00", "open": "1307.42004",
           "high": "1307.71997", "low": "1307.34998", "close": "1307.66003"},
          {"datetime": "2022-08-10 01:00:00", "open": "1307.22498",
           "high": "1307.69995", "low": "1306.59998", "close": "1307.38000"},
          {"datetime": "2022-08-10 00:00:00", "open": "1.53003",
           "high": "1307.05505", "low": "1306.25500", "close": "1306.79004"}]

# a = sorted(values, key=lambda x: x["datetime"])
# print(values[0]["datetime"])
# values.sort(key=lambda x: x["datetime"], reverse=True)
# # print(a)
# # print(values is a)
# values[0]["datetime"] = "QQQQ"
# print(values[0]["datetime"])


c = max(values, key=lambda x: x["high"])["high"]
d = min(values, key=lambda x: x["low"])["low"]
s = sum(values, key=lambda x: x.get("volume"))

print(c, d)

# open = values[0]["open"]
# close = values[-1]["close"]
# print(open, close)

high, low = [], []
for value in values:
    high.append(value["high"])
    low.append(value["low"])
print(max(high), min(low))

# # last_data = "2022-08-10 00:00:10"
# # q = datetime.strptime(
# #     last_data, "%Y-%m-%d"
# # ).date()

# # print(q)

# # a = [None, None]
# b = [1]

# print([] == False)
# print([] is False)
# print([0] is True)
# print([0] == True)
# print(bool([0]), bool([]))
# a = [0, 0, 0, 1]
# b = []
# c = 0
# d = None
# if a:
#     c = sum(a)
# if b:
#     d = sum(b)

# print(c, d)
