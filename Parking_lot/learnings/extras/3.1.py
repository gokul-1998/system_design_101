class Parent:
  def __init__(self, txt):
    print("parent constructor")
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    print("child constructor")
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()

# predict the output
# child
# parent
# hello