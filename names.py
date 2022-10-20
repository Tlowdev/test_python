from name_function import get_formatted_name 



print("Enter 'q' to quit")
while True:
    first = input("Please enter your first name. ")
    if first == 'q':
        break
    last = input("Please enter your last name. ")
    if last == 'q':
        break
    middle = input("Please enter you middle name. ")
    if middle == 'q':
        break
    formatted_name = get_formatted_name(first, last, middle)
    print(f"\nNeatly formatted name: {formatted_name}")