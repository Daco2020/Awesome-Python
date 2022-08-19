import pendulum

def a():
    ...
    with open('histories.csv', 'a') as file:
        for i in range(3):
            locals()[f"변수{i}"] = "locals"
            globals()[f"변수{i*100}"] = "globals"
            c = "c"


a()

# print(locals()[f"변수{1}"])
# print(변수100)
# print(c)



d = pendulum.datetime(2017, 9, 24)
e = pendulum.from_format("2017-09-24", 'YYYY-MM-DD')
print(type(d), type(e), d==e, e)