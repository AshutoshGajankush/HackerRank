"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    if head == None:
        pass
    else:
        s = []
        temp = head
        while(temp!=None):
            s.append(temp.data)
            temp = temp.next
        for i in range(len(s)):
            print s.pop(-1)

  
  
  
  
