from urllib import parse


code = "USD%2FKRW"
a = parse.unquote(code)
# print(code, a)


values = [
    {"datetime": "2022-08-24", "open": 1},
    {"datetime": "2022-08-24", "open": 2},
    {"datetime": "2022-08-23", "open": 3},
]

a = []
temp_date = ""
for i in values:
    if temp_date != i["datetime"]:
        a.append(i)
    temp_date = i["datetime"]

print(a)
