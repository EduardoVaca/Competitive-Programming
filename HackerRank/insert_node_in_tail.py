"""
PROBLEM: Insert a Node at the Tail of a Linked List
from: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list


 Insert Node at the end of a linked list
 head pointer input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method
"""
def Insert(head, data):
    if head == None:
        head = Node(data)
    else:
        current = head
        while current.next != None:
            current = current.next
        current.next = Node(data)
    return head
