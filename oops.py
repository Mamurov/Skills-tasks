
"""
The basic shape class is given. The following Triangle, Square and Circle classes are inherited from it.A triangle is created with the specified base and height.
A square is created with a length of. A circle is created with a radius. Define an abstract method for calculating the area in the base class, and redefine it in the child classes.
Define the get_shape_area() function, which takes a shape and calls the appropriate method to calculate the area.
"""

# class Shape:
#     pass
#
#
# class Triangle(Shape):
#     def __init__(self, height, base):
#         self.height = height
#         self.base = base
#
#     def get_shape_area(self):
#         result = (self.height * self.base) / 2
#         print(result)
#
#
# class Square(Shape):
#     def __init__(self, length):
#         self.length = length
#
#     def get_shape_area(self):
#         result1 = (self.length ** 2)
#         print(result1)
#
#
# class Circle(Shape):
#     def __init__(self, radios):
#         self.radios = radios
#
#     def get_shape_area(self):
#         pi = 3.14
#         result2 = round((self.radios ** 2) * pi)
#         print(result2)
#
#
# triangle = Triangle(4, 5)
# square = Square(12)
# circle = Circle(14)
#
# triangle.get_shape_area()
# square.get_shape_area()
# circle.get_shape_area()


"""
Create 3 classes: Person, Employee and Student, while Employee and Student are inherited from Person. Define the get_info() method in 3 classes:
- for the Person class, it should return the following: "Hi, my name is Ivan Petrov”
- for the Employee class, it should return: "Hi, my name is Ivan Petrov, I work in the company "Horns and Hooves" as a "director”
- for the Student class, it should return: "Hello, my name is Ivan Petrov, I am studying at KSTU
in the 3rd year” Define the get_human_info() function, which will call the get_info method and print the result.
"""


# class Person:
#
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#
#     def get_info(self):
#         print(f" Hello, my name is {self.name} {self.last_name}")
#
#
# class Employee(Person):
#
#     def __init__(self, name, last_name, work, status):
#         Person.__init__(self, name, last_name)
#         self.work = work
#         self.status = status
#
#     def get_info(self):
#         print(f'Hello, my name is {self.name} {self.last_name}, I work for a company {self.work} on the position {self.status}')
#
#
# class Student(Person):
#
#     def __init__(self, name, last_name, university, cours):
#         Person.__init__(self, name, last_name)
#         self.university = university
#         self.cours = cours
#
#     def get_info(self):
#         print(f'Hello, my name is {self.name} {self.last_name}, i study at{self.university} on {self.cours}')
#
#
# person = Person(name='Ivan', last_name='Ivanov')
# employee = Employee(name='Ivan', last_name='Petrov', work="'medium'", status='director')
# student = Student(name='Ivan', last_name='Petrov', university='KSTU', cours  ='3rd')
#
#
# def get_human_info(person):
#     person.get_info()
#
#
# get_human_info(employee)
# get_human_info(student)
# get_human_info(person)

"""
Create 2 classes: MyInt and myString, inherit MyInt from int, myString from str. For both classes, redefine the method that is responsible for working with the “+” operator.
Write the add_objects() function, which accepts an object of one of 2 types. When adding objects of the MyInt class, the message “This is addition”, and
then go the logic of adding 2 numbers, and the output of the result. When concatenating objects of the myString() class, a message should be issued: "This
is concatenation”, and then the logic of concatenation from the base class and the output of the result.
"""

# class MyInt(int):
#
#     def __init__(self, text:int):
#         self.text = text
#
#     def add(self, other):
#         print('This is addition')
#         summ = self.text + other
#         print(summ)
#
#
# class MyString(str):
#
#     def __init__(self, text:str):
#         self.text = text
#
#     def add(self, other):
#         print('This is a concatenation')
#         summ = self.text + other
#         print(summ)
#
#
# integer = MyInt(78)
# integer.add(45)
# string = MyString('Hel')
# string.add('lo')
