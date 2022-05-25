import sqlite3

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs): # 싱글톤 생성 로직
        if cls not in cls._instances: 
            cls._instances[cls] = super(MetaSingleton,\
                cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

db1 = Database().connect()
db2 = Database().connect()

print(f"{db1=}")
print(f"{db2=}")

"""
결과값. 동일한 커서 객체를 사용한다.
db1=<sqlite3.Cursor object at 0x1054045c0>
db2=<sqlite3.Cursor object at 0x1054045c0>
"""