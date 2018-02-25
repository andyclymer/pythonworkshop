
size(200, 200)

for x in range(0, 200, 25):
    for y in range(0, 100, 33):
    
        print("x" + str(x) + " y" + str(y))
        fill(x/164, y/100, x/400)
        rect(x, y, x/10+3, y/5+5)