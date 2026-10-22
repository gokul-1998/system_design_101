class Bla:
    pass


def check(self):
    if not hasattr(self, "initialized"):
        print("not initialized")
    else:
        print("initialized is ther")


bla=Bla()
check(bla)
bla.initialized="huha"
print(bla.initialized)
check(bla)



