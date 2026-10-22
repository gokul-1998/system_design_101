class Database:
    _instance = None

    def __new__(cls):#creates an object.
        print("huha")
        if cls._instance is None:
            
            cls._instance = super().__new__(cls)#creates an object.

        return cls._instance



db1 = Database()
print("line 14")
db2 = Database()
print("line 15")

print(db1 is db2)  # True
print(id(db1) == id(db2))  # True
print(id(db1))
print(id(db2))