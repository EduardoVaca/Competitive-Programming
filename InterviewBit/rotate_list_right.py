# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def list_size(head):
    count = 0
    while head != None:
        count += 1
        head = head.next
    return count

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        B %= list_size(A) 
        if B == 0:
            return A
        last = start = A
        wait = 0
        while last.next != None:
            if wait < B:
                wait += 1
            else:
                start = start.next
            last = last.next
        temp = start.next
        start.next = None
        last.next = A
        return temp