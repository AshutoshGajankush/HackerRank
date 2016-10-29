"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    temp = head
    count = 0
    if position == 0:
        head = Node(data, temp)
        return head
    else:
        while count<position-1 and temp.next != None:
            count=count+1
            temp = temp.next
        if temp.next == None:
            temp.next = Node(data, None)
            return head
        else:
            temp1 = temp.next
            temp.next = Node(data, temp1)
            return head
  
  
  
  
  
  
  
  
