"""
PROBLEM: Delete a Node
from: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list

Delete Node at a given position in a linked list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Delete(head, position):
    if position == 0:
        head = head.next
    else:
        current = head.next
        previous = head
        counter = 1
        while counter != position and current != None:
            previous = current
            current = current.next
            counter += 1
        previous.next = current.next
    return head
