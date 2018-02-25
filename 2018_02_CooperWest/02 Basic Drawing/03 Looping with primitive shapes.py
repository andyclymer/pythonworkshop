import random

size(200, 200)

for number in range(20):
    print(number)
    print(number*5)
    print("Hello!")
    
    fill(number/20, 0, 0, 0.1)
    rect(number*10, number*26, number*23, number*-16)
    
    stroke(0, 0, 1)
    strokeWidth(number/5)
    line((number*7, 0), (100, number*10))
    stroke(None)