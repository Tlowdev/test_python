#1: Reverse a list in Python
list1 = [300, 420, 365, 360, 180]
list1.reverse()
print(list1)

#2: Concatenate two lists index-wise
list2 = ["M", "na", "i", "Ke"]
list3 = ["y", "me", "s", "lly"]
list4 = [i + l for i, l in zip(list2,list3)]
print(list4)

#3: Turn every item of a list into its square
numbers = [1, 2, 3, 4, 5]
square = []
for i in numbers:
    square.append(i * i)
print(square)

#4: Concatenate two lists in the following order
list5 = ["Hello ", "take "]
list6 = ["Dear", "Sir"]
#['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list7 = [x + y for x in (list5) for y in (list6)]
print(list7)

#5: Iterate both lists simultaneously
list8 = [10, 20, 30, 40]
list9 = [100, 200, 300, 400]
for (a, b) in zip(list8, list9[::-1]):
    print(a, b)

#6: Remove empty strings from the list of strings
list10 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
listmod = list(filter(None, list1))
print(listmod)

#7: Add new item to list after a specified item
list11 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list11[2][2].append(7000)
print(list11)

#8:  Extend nested list by adding the sublist
list12 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
sub_list = ["h", "i", "j"]
for i in sub_list:
    list12[2][1][2].append(i)
print(list12)

#9: Replace list’s item with new value if found
list13 = [5, 10, 15, 20, 25, 50, 20]
list13[3] = 200
print(list13)

#10:  Remove all occurrences of a specific item from a list.
list14 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list14:
    list14.remove(20)
    print(list14)
