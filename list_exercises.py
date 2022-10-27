#1: Reverse a list in Python
list1 = [300, 420, 365, 360, 180]
list1.reverse()
print(list1)

#2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + l for i, l in zip(list1,list2)]
print(list3)

#3: Turn every item of a list into its square
numbers = [1, 2, 3, 4, 5]
square = []
for i in numbers:
    square.append(i * i)
print(square)

#4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
#['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list3 = [x + y for x in (list1) for y in (list2)]
print(list3)

#5: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for (a, b) in zip(list1, list2[::-1]):
    print(a, b)

#6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
listmod = list(filter(None, list1))
print(listmod)

#7: Add new item to list after a specified item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#8:  Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
sub_list = ["h", "i", "j"]
for i in sub_list:
    list1[2][1][2].append(i)
print(list1)

#9: Replace list’s item with new value if found
list1 = [5, 10, 15, 20, 25, 50, 20]
list1[3] = 200
print(list1)

#10:  Remove all occurrences of a specific item from a list.
list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
    list1.remove(20)
    print(list1)
