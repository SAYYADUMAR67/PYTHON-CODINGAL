class IOSinput():
    def __init__(self):
        self.str1 = ""
    def getstring (self):
        self.str1 = input("enter a string")
    def print_string(self):
        print("the result is",self.str1.upper())
str1 = IOSinput()
str1.getstring()
str1.print_string()