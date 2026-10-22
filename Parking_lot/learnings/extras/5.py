class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.connected = True


db1 = Database()
db1.connected = False
    # True
print(db1.connected)
db2 = Database()
print(db1.connected)

# print(db1 is db2)       # True
print(db2.connected)    # True