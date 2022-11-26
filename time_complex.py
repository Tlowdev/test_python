# Time complexity algorithm is the amount of time it takes to run a function, the length
# of the input.
# The length of the input determines how many operations the algorithm will do.
# This provides information on wether the number of operations of an algorithm
# increases or decreases execution time.
# constant time complexity = O(1)
# linear time complexity = O(n)
# logarithmic time complexity = O(log n)
# quadratic time complexity = O(n^2)
# insertion sort best case = O(n) worst case is O(n^2)
# Merge sort always = O(nlogn)
# Quick sort best case = O(nlogn) worst case is O(n^2)
# Bubble sort best case = O(n) worst case is O(n^2)
# Linear search best case = O(1) worst case is O(n)
# Binary search best case = O(1) worst case is O(log n)


# constant time complexity example algorithm
def fun():
    val = 1
    print(f"Value = {val}")


# linear time complexity
# when runtime of algorithm rises linearly with the length of the input
# when function checks all values of input O(n) 
def loop():
    ex_list = [1, 4, 6, 8, 0]
    for i in ex_list:
        print(i)


# Logarithmic time complexity
# When an algorithm lowers the amount of input
# in each step o(log n)
# Binary search trees and binary search functions

#
#
#


# quadratic time complexity
# when execution time runs non linearly with length of input
# nested loops are quadratic where one loop is O(n)
# O(n)*O(n) = O(n^2)
def nested_loop():
    start = ['ready', 'set', 'go']
    for i in start:
        print(i)
        for j in i:    
            print(j)
