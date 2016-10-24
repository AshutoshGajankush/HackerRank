# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

arr = []
# Converting input into array
for line in sys.stdin:
    new_list = [int(elem) for elem in line.split()]
    arr.append(new_list)  
n, d = arr.pop(0)
array = arr.pop(0)

#Left rotation using Pop and append
for i in range(d):
    element = array.pop(0) # Poppping the first element
    array.append(element) # appending the popped element to the end of the list

# Printing the values in the desired format
for values in array:
	print values,