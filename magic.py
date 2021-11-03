
"""
Write a class MyList that inherits from list. Make indexing
elements started at 1.

"""

# class MyList (list):
#     def getitem(self, index):
#         return super(MyList, self).getitem(index - 1)
#
#     def setitem(self, index, val):
#         super(MyList, self).setitem(index - 1, val)
#
#     def delitem(self, index):
#         super(MyList, self).delitem(index - 1)
#
#
# x = MyList([1, 2, 3, 4, 5])
# print(x)
# print(x[1])
# print(x[2])
# print(x[3])

"""
Write a Student class that describes the student. The student has the following attributes: first name, last name, class,
and subject grades in the following form: {'history’: 89, history’: 89‘ 'history’: 89, math’: 100‘ 'history’: 89, literature’: 88}.
Make it so that students are compared with each other according to the student's average grade in subjects.

"""

# class Student:
#     def __init__(self, name, lastname, group, scores):
#         self.name = name
#         self.lastname = lastname
#         self.group = group
#         self.scores = {'history': 89, 'math': 100, 'literature': 88}
#         print(self.scores)

#     def get_info(self):
#         return f"{self.name} {self.lastname} is studying at {self.group}"

#     def get_average(self, scores):
#         print(self.scores)

#         self_scores=list(self.scores.values())
#         mean = sum(self_scores)/(round(len(self_scores)))
#         return f'Average rating {mean}'


# student = Student(name='Rus', lastname='Avtandilov', group='group-2', scores={})
# print(student.get_info())
# print(student.get_average({'history': 78, 'math': 100, 'literature': 80}))





