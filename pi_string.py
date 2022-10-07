#File containing pi with 1m decimals
file_name = 'text_files/pi_1m.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

#creating empty string to pass the file to
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

#created a variable with my birthday (mmddyyyy)
my_b_day = '04281990'


if my_b_day in pi_string:
    print('My birthday appears in the 1st million digits of pi!')
else:
    print('My birthday is not in pi.')


#print(pi_string)
print(len(pi_string))
