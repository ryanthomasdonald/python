# OOP

# History

# Assembly Language
# Very basic, used for modern drivers

# Structured Programming
# Loops, etc.

# 3 main problems with S.P.:
# Emphasis on functionality, not data
# Limitations
# Gap in dev-to-client communication

# Data is the most important part of a program
# Companies pay big money to protect it

# 30K lines of code is the line in the sand for safety, communication

# Building blocks (pillars) of OOP:
# Objects
# Classes
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism

# Objects:
# Represent real life
# attributes = properties
# behavior = functionality

# Inheritance
# Parent --> Child       # Just like humans

# class Student:
#     # Constructor is type of method that is called as soon as an object is created
#     def __init__(self):
#         print("I am a constuctor.")
# # a function inside of "class" is called a "method"
#     def say_hello(self):      # self is a reference to address of variable, don't worry about it, just ALWAYS use
#         print("Hello.")
# # Creating an object from template^^^:

# matt = Student()       # instantiated (created) an object
# matt.say_hello()       # period is called "dot operator"

# victoria = Student()
# victoria.say_hello()

# stephen = Student()
# stephen.say_hello()

# mercer = Student()
# mercer.say_hello()

# # Printing "Hello" and then a name
# class Student:                                    # Good practice to capitalize a class name (Student)
#     # Constructor (see "init" syntax)
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name             # "Instance variables", they are global to the class
#         self.last_name = last_name
#     def say_hello(self):      # self is a reference to address of variable, don't worry about it, just ALWAYS use
#         print(f"Hello, {self.first_name} {self.last_name}.")

# matt = Student("Matt", "Fisher")
# victoria = Student("Victoria", "Walker")
# stephen = Student("Stephen", "Doty")
# mercer = Student("Mercer", "Mahaffey")           # instantiated (created) an object

# matt.say_hello()       # period is called "dot operator"

# victoria.say_hello()

# stephen.say_hello()

# mercer.say_hello()

# # Lab 1:
# # Do 1 and 2
# class Person:
#     def greeting(self, first_name):
#         print(f"Good morning, {first_name}.")

# matt = Person()
# victoria = Person()

# matt.greeting("Matt")
# victoria.greeting("Victoria")

# # Buttons:
# class Button:                                    # contains basic functionality of buttons
#     # constructor
#     def __init__(self, color, name):             # remember to put "self", used for global start-up tasks
#         self.color = color
#         self.click = 0                           # called "instance variables"
#         self.name = name
#     # methods
#     def show_info(self):
#         print(f"{self.color} {self.name} {self.click}")
    
#     def do_click(self):
#         self.click += 1
#         print(f"Number of clicks: {self.click}")

# nav_button = Button("yellow", "Nav")
# nav_button.show_info()
# nav_button.do_click()
# nav_button.do_click()
# nav_button.do_click()

# help_button = Button("red", "Help")
# help_button.show_info()
# help_button.do_click()

# pay_button = Button("green", "Pay")
# pay_button.show_info()
# pay_button.do_click()
# pay_button.do_click()

# # Labs:
# class Student:
#     # constructor
#     def __init__(self, name):
#         self.name = name
#         # print("Constructor")
#     # methods
#     def greeting(self):
#         print(f"Good morning, {self.name}.")

# matt = Student("Matt")
# matt.greeting()

# victoria = Student("Victoria")
# victoria.greeting()

# class GoogleMaps:
#     earth_radius = 10000000                 # "class variable" = global value (literally, in this case)
#     def __init__(self, addr1, addr2):
#         self.addr1 = addr1
#         self.addr2 = addr2
#         self.lat = None
#         self.lon = None

#     def convert(self):
#         pass

#     def map():                              # with no "self", it cannot access any of the instance variables
#         print("determining Google map")

# #Lab
# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone

#     def greet(self, other_person):
#         print(f'Hello {other_person.name}. I am {self.name}!')

# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")        # info pulled in by line below

# sonny.greet(jordan)                                                # "jordan" (lowercase) is an object, not a string
# jordan.greet(sonny)
# print(f"{sonny.name}: {sonny.email} {sonny.phone}")
# print(f"{jordan.name}: {jordan.email} {jordan.phone}")

# Protecting Data
# Public
# Private
# Protected
# Internal

# # Name mangling in Python:
# class Test:
#     def __intit__(self):
#         self._a = "a"                      # Pretends that variable is private in Python, let's other devs know
#         self.__b = "b"                     # Is actually private, but can still be used in code

# # INHERITANCE:
# # Parent --> Child
# class Animal:                             # Parent (or Base) Class
#     def __init__(self, name):
#         self.name = name
    
#     def who_am_i(self):
#         print("I am an animal.")

# class Dog(Animal):                        # Child Class, NOTICE SYNTAX!!!
#     def woof(self):
#         print("wolf")

# fido = Dog("Pickle")

# fido.woof()
# fido.who_am_i()

# class OurString(str):                       # Includes functionality built-in to string class
#     def __init__(self, word):
#         self.word = word
    
#     def reverse(self):
#         rev_string = ""
#         for char in self.word:
#             rev_string = char + rev_string
#         return rev_string

# my_string = OurString("hello")
# print(my_string.reverse())

# class Car:
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
    
#     def greeting(self):
#         print("\nCar Details:")
    
#     def car_details(self):
#         print(f"{self.make}, {self.model}, {self.color}")

# class Hybrid(Car):
#     def __init__(self, mpg, make, model, color):
#         self.mpg = mpg
#         super(Hybrid, self).__init__(make, model, color)

#     def car_type(self):
#         print(f"I'm a hybrid and I get {self.mpg} MPG.")

# class Electric(Car):
#     def __init__(self, battery, make, model, color):
#         self.battery = battery
#         super(Electric, self).__init__(make, model, color)

#     def car_type(self):
#         print(f"I'm electric and my battery is {self.battery}.")

# prius = Hybrid(34, "Toyota", "Prius", "Green")                     # typing "Car" not necessary, inheritance in action!
# prius.greeting()
# prius.car_details()
# prius.car_type()

# tesla = Electric("full", "Tesla", "Model-S", "Purple")
# tesla.greeting()
# tesla.car_details()
# tesla.car_type()

# 3 ways that the parent and child classes can interact:
# 1. Actions on the child imply an action on the parent.
# 2. Actions on the child override the action on the parent.
# 3. Actions on the child alter the action on the parent.

# COMPOSITION:
class Student:
    def __init__(self, first_name, last_name, campus):
        self.first_name = first_name
        self.last_name = last_name
        self.campus = campus

    def printStudent(self):
        print(f"{self.first_name} {self.last_name} campus: {self.campus}")

class Campus:
    def __init__(self):
        self.students = []                  # holds all of the students

    def add_student(self, first_name, last_name, campus):
        student_obj = Student(first_name, last_name, campus)
        self.students.append(student_obj)

    def show_current_students(self):
        for student_obj in self.students:
            print(f"{student_obj.first_name} {student_obj.last_name} {student_obj.campus}")

    def get_no_of_students(self):
        print(len(self.students))

atlanta = Campus()

atlanta.add_student("Emily", "Ye", "Atlanta")
atlanta.add_student("Hunter", "Hutchisson", "Atlanta")
atlanta.add_student("James", "Ivy", "Atlanta")

atlanta.show_current_students()
atlanta.get_no_of_students()