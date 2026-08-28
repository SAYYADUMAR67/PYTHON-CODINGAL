from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("passed value:",x)
    @abstractmethod
    def task(self):
        print("we are venom")
class test_class(Absclass):
    def task(self):
        print("we are carnage")
test_obj = test_class()
test_obj.task()
test_obj.print(100)