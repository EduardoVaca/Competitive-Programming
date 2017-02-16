"""
PROBLEM: Remove Friends
from: hackerearth.com
"""

class Node(object):

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def create_list():
    friends = [int(x) for x in input().strip().split(' ')]
    head = Node(friends[0])
    current = head
    for e in friends[1:]:
        new_node = Node(e, None, current)
        current.next = new_node
        current = current.next
    return head

def print_list(head):
    current = head
    while current != None:
        if current.next == None:
            print('{}'.format(current.data))
        else:
            print('{} '.format(current.data), end='')
        current = current.next

def eliminate_friends(head, n_friends):
    current = head
    deleted = False
    while current != None:
        if current.next == None:
            current.prev.next = None
            current = current.prev
            deleted = True
        elif current.data < current.next.data:
            if current.prev == None:
                head = current.next
                head.prev = None
                current = head
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                current = current.prev
            deleted = True
        else:
            current = current.next
            deleted = False
        if deleted:
            n_friends -= 1
            if n_friends == 0:
                return head


n = int(input().strip())
for i in range(n):
    friends, eliminate = [int(x) for x in input().strip().split(' ')]
    head = create_list()
    head = eliminate_friends(head, eliminate)
    print_list(head)
