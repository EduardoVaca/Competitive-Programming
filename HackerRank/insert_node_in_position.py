"""
PROBLEM: Insert a node at a specific position in a linked list
from: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list

Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
 """

""" Special cases:
head is None
position is 0
"""
def InsertNth(head, data, position):
    if head == None:
        head = Node(data)
    elif position == 0:
        newNode = Node(data, head)
        head = newNode
    else:
        current = head.next
        previous = head
        counter = 1
        while current != None:
            if position == counter:
                break
            counter += 1
            previous = current
            current = current.next
        newNode = Node(data, current)
        previous.next = newNode
    return head
