from dataclasses import dataclass
from datetime import timedelta, datetime
from dataclasses import dataclass
from datetime import datetime, timedelta

a = datetime(2020, 12, 12, 0, 0, 0)
b = datetime(2025, 12, 12, 0, 0, 0)

c = b-a

@dataclass(frozen=True)
class date:
    date: timedelta

d = date(c)
print(d.date)

# 1826 days, 0:00:00
d.c = 2
print(d.c)
