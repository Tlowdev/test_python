#example file path
ex_file_path = 'text_files/pi_digits.txt'

#file program, opens file, 
#reads file as string, and prints file to console.
with open(ex_file_path) as file_object:
   contents = file_object.read()
   print(contents.rstrip())


#reads file as list .readlines() then loops 
#and prints removing whitespace .rstrip()
with open(ex_file_path) as file_object:
    content = file_object.readlines()
    for line in content:
        print(line.rstrip())


#reads file line by line as string
with open(ex_file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

