class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.connected = True
            self.initialized = True


db1 = Database()
db1.connected = False

db2 = Database()

print(db1 is db2)       # True
print(db2.connected)    # False