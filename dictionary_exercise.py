#1 convert 2 lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
this_dict = zip(keys, values)
d = dict(this_dict)
print('ex 1', d)
#example solution
#res_dict = dict(zip(keys, values))


#2 merge 2 python dictionaries into 1
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print('ex 2', dict1)
#example solution
#dict3 = {**dict1, **dict2}


#3 print value of key 'history' in dictionary
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print('ex 3', sampleDict['class']['student']['marks']['history'])

#4 initialize a dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
this_dict = dict.fromkeys(employees, defaults)
print('ex 4', this_dict)

#5 Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
key = ["name", "salary"]
new_dict = {k: sample_dict[k] for k in key}
print('ex 5', new_dict)

#6 Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]
for k in keys:
    sample_dict.pop(k)
print('ex 6', sample_dict)

#7 Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
v = sample_dict.values()
for value in v:
    if value == 200:
        print('ex 7: 200 was found in dictionary')
#example solution
#if 200 in sample_dict.values():
#   print('200 present in a dict')


#8 Rename key of a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict['location'] = sample_dict['city']
del sample_dict['city']
print('ex 8', sample_dict)
#example solution
#sample_dict['location'] = sample_dict.pop('city')


#9 Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print('ex 9', min(sample_dict))
#example solution
#print(min(sample_dict, key=sample_dict.get))


#10 Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary'] = 8500
print('ex 10', sample_dict)