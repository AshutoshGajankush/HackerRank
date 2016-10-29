#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
out=[]

for i in range(1,(len(arr)-1)):
    for j in range(1,(len(arr)-1)):
        sum = arr[i-1][j-1]+ arr[i-1][j] + arr[i-1][j+1]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]+arr[i][j]
        out.append(sum)
print max(out)  
            
        