def roundint(number):
    # returns rounded integer number
    return int(round(number))


def calculate_sum(number_1, number_2):
    if type(number_1) == int and type(number_2) == int:
        return number_1 + number_2
    else:
        print("that's not a number!")


print(calculate_sum(1, 2))
print(calculate_sum(-1000, 10000))
print(calculate_sum(-1000, 'Peter'))
