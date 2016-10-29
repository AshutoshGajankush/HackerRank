#Body
"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    tempA = headA
    tempB = headB
    flag = 1
    while(tempA != None or tempB != None):
        if tempA == None or tempB == None:
            return 0
        if tempA.data != tempB.data:
            flag = 0
        tempA = tempA.next
        tempB = tempB.next
    if flag == 0:
        return 0
    else:
        return 1