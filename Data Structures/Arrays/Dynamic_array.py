import sys

arr = []
# Converting input into array
for line in sys.stdin:
    new_list = [int(elem) for elem in line.split()]
    arr.append(new_list)     

# Setting the Number of sequence and Number of Queries
N,Q = arr.pop(0)
lastAns = 0
seq = []

#Initialising N empty lists to seq list
for j in range(N):
    seq.append([])

for i in range(Q):
    x = arr[i][1] 
    y = arr[i][2]
    if (arr[i][0] == 1):              # checking query type  
        index = (x^lastAns)%N         # Finding the index of seq to add the value 
        seq[index].append(y)
    elif(arr[i][0] == 2):             # checking query type
        index = (x^lastAns)%Number    # Finding the index of seq to search for a value.
        index1 = y%len(seq[index])    # Finding the index of the value   
        lastAns = seq[index][index1]  # Assigning Last answer
        print lastAns                 # Printing LastAns
    