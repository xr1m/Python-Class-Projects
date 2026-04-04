# Abstract Class:

from abc import ABC, abstractmethod

class base(ABC):
    def func1(self, x):
        print(f"The passed value: {x}")
    @abstractmethod
    def func2(self):
        print("I am an abstract class.")

class derived(base):
    def func2(self):
        print("I am inside a derived class.")

obj1 = derived()
obj1.func2()
obj1.func1(100)