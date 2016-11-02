"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def MergeLists(headA, headB):
    temp = Node(0)
    head = temp
    while headA!=None or headB != None:
        if headA == None:
            temp.next = headB
            headB = headB.next
            temp = temp.next
            continue
        if headB == None:
            temp.next  = headA
            headA = headA.next
            temp = temp.next
            continue
        if headA.data <= headB.data:
            temp.next = headA
            headA = headA.next
            temp = temp.next
        else:
            temp.next = headB
            headB = headB.next
            temp = temp.next
    return head.next
