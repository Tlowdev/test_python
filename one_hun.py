#simple prog that give the year you turn 100
import random

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

#ex 6
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


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [x for x in a if x in b]
print(c)
