
import datetime

from pytz import timezone
matching_code = {
    "GSPC": "s&p500",
    "DJI": "dow30",
    "IXIC": "nasdaq",
    "HSI": "hangseng",
    "000001": "shanghai",
    "N225": "nikkei225",
}

codes = ["000001", "asd"]

for code in codes:
    a = matching_code.get(code, code)
    print(a)


a = timezone("America/New_York")
b = timezone("US/Eastern")


today = datetime.datetime.now()
a = today.astimezone(a)
b = today.astimezone(b)
print("America/New_York :", a)
print("US/Eastern :", b)
