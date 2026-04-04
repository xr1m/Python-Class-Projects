# Class Animal:

from abc import ABC, abstractmethod

class Animal(ABC):
    def func1(self):
        pass

class Human(Animal):
    def func1(self):
        print("I can walk and run")

class Birds(Animal):
    def func1(self):
        print("I can fly and walk")

class Sea_Animals(Animal):
    def func1(self):
        print("I can swim and breathe in water.")

obj1 = Human()
obj1.func1()

obj2 = Birds()
obj2.func1()

obj3 = Sea_Animals()
obj3.func1()