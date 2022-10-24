#1 create a function that takes 2 arguments, name and age
def fun1(name, age):
    print(f"Hello my name is {name}, I am {age} years old.")

fun1('Abby', 24)

#2 create a function with variable length of arguments
def fun2(*args):
    for x in args:
      print(x)

fun2('blue', 42, 'set', 'hike')

#3 return multiple values from a function accepts 2 varibales adds and subtracts
def fun3(x, y):
    add = x + y
    subtract = x - y
    print(f"Subtract: {subtract}")
    print(f"Add: {add}")

fun3(56, 34)

#4 Create an argument with a default value
def fun4(name, salary= 90_000):
    print(f"{name}'s occupation is software engineer and makes {salary} a year.")
fun4('Jim')

#5 Create an inner function to calculate the addition
def fun5(a, b):
    c = a + b
    def fun():
        d = c + 5
        print(d)
    fun()
fun5(10,5)

#6 Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def fun6(num):
    if num <= 1:
        return num
    else:
        return num + fun6(num - 1)
n = 10
if n < 0:
    print("Please enter a positive number.")
else:
    print(f"The sum of recursive 10 is: {fun6(n)}")

#7 Assign a different name to a function and call it using the new name.
def car(name, year):
    print(f"Car: {name}\nYear: {year}")
new_car = car
new_car('Acura', 1990)

#8 Generate a list of all even numbers between 4 and 30
def fun8():
    fun = list(range(4, 31))
    run = []
    for num in fun:
        if num % 2 == 0:
            run.append(num)
    print(run)
fun8()

def fun9():
    x = [4, 6, 8, 24, 12, 2]
    print(max(x))
fun9()