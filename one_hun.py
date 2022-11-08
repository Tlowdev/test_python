#simple prog that give the year you turn 100
import random
import array

#ex 1
name = input('What is your name? ')
age = int(input('What is your age? '))
cpy_num = int(input('Enter a number of copies '))
#current_year = 2022

#ex 2
def when_hun(name, age, cpy_num, current_year = 2022):
    one_hun = 100 - age + current_year
    for i in range(cpy_num):
        print(f"{name}! You will be 100 in the year: {one_hun}!")
when_hun(name, age, cpy_num)

#ex 3
print('\ndetermines if the number is odd even or divisible by 4')
def even_odd(cpy_num):
    if cpy_num % 4 == 0:
        print(f"The number: {cpy_num} is divisible by 4")
    elif cpy_num % 2 == 0:
        print(f"The number: {cpy_num} is even.")
    else:
        print(f"The number: {cpy_num} is odd.")
even_odd(cpy_num)

#ex 4
print('\nprints from list, numbers less than your selected number ')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [x for x in a if x < cpy_num]
print(b)

#ex 5
print('\nthese numbers are divisible by your number')
divisor = list(range(1, cpy_num))
div_list = [x for x in divisor if cpy_num % x == 0]
print(div_list)

#ex 6 ref ex 10
print('\n sharing common from 2 lists into 1')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for x in a:
    if x in b:
        c.append(x)
print(c)

#ex 7
print('\nThis is a copy of a list')
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
copy = a[:]
print(copy)

#ex 8
#rock paper scissors
possible_actions = ['rock', 'paper', 'scissors']
def rock_paper_scissors():
    player = input('\nrock, paper, or scissors? ')
    computer = random.choice(possible_actions)
    if player == computer:
        print("Tie game")
    elif player == 'rock' and computer == 'scissors':
        print("Rock smash scissors player wins")
    elif player == 'rock' and computer == 'paper':
        print("paper covers rock computer wins")
    elif player == 'paper' and computer == 'rock':
        print("paper covers rock player wins")
    elif player == 'paper' and computer == 'scissors':
        print('scissors cut paper computer wins')
    elif player == 'scissors' and computer == 'rock':
        print("Rock smash scissors computer wins")
    elif player == 'scissors' and computer == 'paper':
        print('scissors cut paper player wins')
rock_paper_scissors()

def playAgainfunc():
    print("To play again press 'Y'. To exit press anything else.")
    playAgainresponse = input()
    if playAgainresponse == 'Y':
        rock_paper_scissors()
        playAgainfunc()
    if playAgainresponse == 'y':
        rock_paper_scissors()
        playAgainfunc()
    else:
        print("Good bye!")
playAgainfunc()

#ex 9
def guessing_game():
    num_nine = random.randint(1, 9)
    pick = input("Select one number 0 - 9: ")
    user = int(pick)
    if num_nine == user:
        print("Lucky guess!")
    elif num_nine > user:
        print(f'Too low: the number was {num_nine}')
    elif num_nine < user:
        print(f'Too high: the number was {num_nine}')
guessing_game()

def playAgainfunct():
    print("To play again press 'Y'. To exit press anything else.")
    playAgainresponse = input()
    if playAgainresponse == 'Y':
        guessing_game()
        playAgainfunct()
    if playAgainresponse == 'y':
        guessing_game()
        playAgainfunct()
    else:
        print("Good bye!")
playAgainfunct()

#ex 10 ref ex 6
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [x for x in a if x in b]
print(c)

#ex 11
def prime(cpy_num):
    num = 6 * cpy_num + 1
    print(f"{num}: is a prime number")
prime(cpy_num)

#ex 12
print("first and last element in list")
a = [5, 10, 15, 20, 25]
b = [a[i] for i in (0, -1)]
print(b)

#ex 13
print(f'Fibonacci up to {cpy_num} you selected')
def fibonacci(cpy_num):
    a, b = 0, 1
    while a < cpy_num:
        print(a)
        a, b = b, a + b
fibonacci(cpy_num)

#ex 14
print('rm doubles from list')
def rm_oc():
   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
   b = []
   for x in a:
    if x not in b:
        b.append(x)
   print(b)
rm_oc()
#converts list to set and back to order list
print('rm doubles from list using set()')
def set_to_rm():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = set(a)
    c = list(b)
    c.sort()
    print(c)
set_to_rm()

#ex 15
print('\nreverse sentence')
dude = "dude, where's your car, where's your car dude."
def reverse_str(dude):
     return ' '.join(dude.split()[::-1])
if __name__ == "__main__":
    input = dude
    print (reverse_str(input))
reverse_str(dude)

#ex 16 random password with length 15
length = 15
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*']
password_leng = digits + capital + lower_case + symbol
rand_digits = random.choice(digits)
rand_capital = random.choice(capital)
rand_lowercase = random.choice(lower_case)
rand_symbol = random.choice(symbol)
temp_pass = rand_digits + rand_capital + rand_lowercase + rand_symbol
for x in range(length - 4):
    temp_pass = temp_pass + random.choice(password_leng)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
password = ''
for x in temp_pass_list:
    password = password + x
print(password)

#ex 17 
