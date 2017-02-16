"""
PROBLEM: Insert a node at the head of a linked list
from: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list

Insert Node at the begining of a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def Insert(head, data):
    if head == None:
        head = Node(data)
    else:
        new_node = Node(data, head)
        head = new_node
    return head
