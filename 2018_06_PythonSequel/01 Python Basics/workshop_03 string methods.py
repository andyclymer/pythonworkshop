from __future__ import print_function

bold_statement = 'Everybody loves Python'

my_list = bold_statement.split()

print(bold_statement)

# string functions
print(bold_statement.replace('Python', 'Beer'))
print(bold_statement.swapcase())
print(bold_statement.upper())
print(bold_statement.lower())
print(bold_statement.strip())

# list stuff
print(my_list)
for word in my_list:
    print(word)
