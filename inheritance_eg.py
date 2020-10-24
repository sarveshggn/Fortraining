class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")

class Dog(Animal):

    def __init__(self):
        print("DOG CREATED")

    def bark(self):
        print("WOOF WOOF!!!")

    def eat(self):
        print("DOG EATING")

mydog = Dog()
mydog.who_am_i()
mydog.eat()
mydog.bark()
