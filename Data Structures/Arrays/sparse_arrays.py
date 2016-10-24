# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

arr = []
# Converting input into array.
for line in sys.stdin:
    new_list = [elem for elem in line.split()]
    arr.append(new_list)  

N = arr.pop(0) 
N = int(N[0]) # Getting the number of strings.
string_list = []
# Making a list of all strings.
for i in range(N):
    list = arr.pop(0)
    string_list.append(list[0])

Q = arr.pop(0)
Q = int(Q[0]) # Getting the number of queries.
querie_list = []
# Making a list of queries.
for j in range(Q):
    list = arr.pop(0)
    querie_list.append(list[0])

# Iterating over the String and Queries to check the availability.
for querie in querie_list:
    count = 0 # Initialising count to 0.
    for string in string_list:
        if(querie == string):
            count = count + 1 # Increment the count when a match is found.
    print count