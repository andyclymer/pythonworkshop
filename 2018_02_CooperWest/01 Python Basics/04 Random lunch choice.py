import random

lunchOptions = ['Pizza', "Sandwiches", "Vietnamese", "Jennies"]

print lunchOptions
lunchOptions.sort()
print lunchOptions[0]

# Random float between 0 and 1
number = random.random()
print(number)
otherNumber = random.randint(5, 20)
print(otherNumber)

lunch = random.choice(lunchOptions)
print(lunch)

lunchOptions.sort()
random.shuffle(lunchOptions)
print(lunchOptions)
