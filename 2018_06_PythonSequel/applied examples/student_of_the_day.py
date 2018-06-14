import random
students = {
    'Flavia': 123,
    'Spencer': 4032,
    'Doug': 9203,
    'Jon': 4,
    'Erica': 39204}


student_of_the_month = random.choice(students.keys())
print(student_of_the_month)

