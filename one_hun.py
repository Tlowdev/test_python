#simple prog that give the year you turn 100
from random import random


name = input('What is your name? ')
age = int(input('What is your age? '))
cpy_num = int(input('Enter a number of copies '))
#current_year = 2022

def when_hun(name, age, cpy_num, current_year = 2022):
    one_hun = 100 - age + current_year
    for i in range(cpy_num):
        print(f"{name}! You will be 100 in the year: {one_hun}!")
when_hun(name, age, cpy_num)

def even_odd(cpy_num):
    if cpy_num % 4 == 0:
        print(f"The number: {cpy_num} is divisible by 4")
    elif cpy_num % 2 == 0:
        print(f"The number: {cpy_num} is even.")
    else:
        print(f"The number: {cpy_num} is odd.")
even_odd(cpy_num)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [x for x in a if x < cpy_num]
print(b)

divisor = list(range(1, cpy_num))
div_list = [x for x in divisor if cpy_num % x == 0]
print(div_list)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for x in a:
    for y in b:
        if x == y:
            c.append(y)
print(c)