"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    lengthA = 0
    lengthB = 0
    tempA = headA
    tempB = headB
    #Calculating the length of two lists.
    while(tempA!=None):
        lengthA = lengthA+1
        tempA = tempA.next
    while(tempB!= None):
        lengthB = lengthB + 1
        tempB = tempB.next
    #Keeping the count for iteration
    count = 0

    tempA = headA
    tempB = headB
    if lengthA>lengthB:
        #If listA > listB
        diff = lengthA-lengthB
        while(count!=diff): # Iterating till both are of same length
            tempA = tempA.next
            count= count+1
        while(tempA != tempB): # Finding the common value where two lists merge
            tempA = tempA.next
            tempB = tempB.next
        return tempA.data # return the merge data
    else:
        #If list B > listB
        count = 0
        diff = lengthB-lengthA
        while(count!=diff): # Iterating till both are of same length
            tempB = tempB.next
            count = count+1
        while(tempA != tempB): # Finding the common value where two lists merge
            tempA = tempA.next
            tempB = tempB.next
        return tempA.data # return the merge data

  
  
  
  
  
  
  
