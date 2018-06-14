from __future__ import print_function

student_names = ['Flavia', 'Spencer', 'Doug', 'Jon', 'Erica']

for name in student_names:
    print(name)
print()

print(student_names[1])
print(student_names[-1])

# range from item 1 to item 3
print(student_names[1:3])
# range from item 1 to the end
print(student_names[1:])

# print every 2nd student name
print(student_names[::2])
# print list in reverse
print(student_names[::-1])

# reverse the data of the actual list
student_names.reverse()
print(student_names)

my_tuple = tuple(student_names)
print(my_tuple)
# this doesn't work, tuples are 'immutable' which means they cannot
# be changed in place:
# my_tuple.reverse()
