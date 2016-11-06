"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    node = Node(data,None,None) # making a new node
    if head==None: # If the list is empty
        return node
    temp = head # making a temp node for eterating
    while(temp.next!=None): # To iterate till the last element
        if(temp.data <= data and temp.next.data >= data): # to find the exact position of the data to be inserted
            node.prev = temp
            node.next = temp.next
            temp.next.prev = node
            temp.next = node
            return head
        temp = temp.next
    # If the data to be inserted at last of the linked list
    node.prev = temp
    temp.next = node
    return head
            
  
  
  
  
  
  
  
  
  
  
