"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    temp = head
    count = 0
    if position == 0:
        head = temp.next
        return head
    else:
        while count<position-1 and temp.next!=None:
            temp = temp.next
            count = count + 1
        if temp.next.next == None:
            temp.next = None
            return head
        else:
            temp1 = temp.next
            temp2 = temp1.next
            temp.next = None
            temp.next = temp2
            return head
  
  
  
  
  
