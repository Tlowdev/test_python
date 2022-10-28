# Use for the questions below:
#nums = [i for i in range(1,1001)]
#string = "Practice Problems to Drill List Comprehension in Your Head."

#1 Find all of the numbers from 1–1000 that are divisible by 8
nums = [i for i in range(1,1001)]
div_by_eight = [num for num in nums if num % 8 == 0]
#print(div_by_eight)

#2 Find all of the numbers from 1–1000 that have a 6 in them
nums = [i for i in range(1,1001)]
num_six = [num for num in nums if "6" in str(num)]
#print(num_six)

#3 Count the number of spaces in a string (use string above)
string = "Practice Problems to Drill List Comprehension in Your Head."
str_space = len([s for s in string if s == " "])
#print(str_space)

#4 Remove all of the vowels in a string (use string above)
string = "Practice Problems to Drill List Comprehension in Your Head."
rm_vowels = ''.join([v for v in string if v not in ['a','e','i','o','u']])
#print(rm_vowels)

#5 Find all of the words in a string that are less than 5 letters (use string above)
string = "Practice Problems to Drill List Comprehension in Your Head."
words = string.split()
less_five = [l for l in words if len(l) < 5]
#print(less_five)

#6 Use a dictionary comprehension to count the length of each word in a sentence (use string above)
string = "Practice Problems to Drill List Comprehension in Your Head."
scissor = string.split()
word_len = {x:len(x) for x in scissor}
#print(word_len)

#7 Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
nums = [i for i in range(1,1001)]
div_num_range = [num for num in nums if True in[True for divisor in range(2, 10) if num % divisor == 0]]
#print(div_num_range)

#8 For all the numbers 1–1000, use a nested list/dictionary comprehension to 
# find the highest single digit any of the numbers is divisible by
nums = [i for i in range(1,1001)]
highest_div = {num:max([divisor for divisor in range(1, 10) if num % divisor == 0]) for num in nums }
print(highest_div)