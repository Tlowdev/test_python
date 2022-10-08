#Program using exceptions takes in user input as a string
#converts to integer then divides and prints to console
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")
while True:
    """Input first number"""
    first_number:str = input("First number: ")
    if first_number == 'q':
        break
    """Input second number"""
    second_number:str = input("Second number: ")
    if second_number == 'q':
        break
    try:
        """Converts first and second number to int then divides"""
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        """This exception wont allow zero and continues"""
        print("You cant divide by zero.")
    except ValueError:
        """This exception wont allow strings and continues"""
        print("You can only use numbers.")
    else:
        print(answer)
        
