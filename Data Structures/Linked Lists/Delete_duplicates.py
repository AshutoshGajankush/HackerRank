"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    if(head == None or head.next == None):
        return head
    temp = head
    while(temp!=None and temp.next!=None):
        if(temp.data == temp.next.data):
            temp.next = temp.next.next
        else:
            temp = temp.next            
    return head