# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        if m == n:
            return A
        start = current = None
        temp_current = A
        for i in range(n):
            if i + 2 == m:
                start = temp_current
            elif i + 1 == m:
                current = temp_current
            temp_current = temp_current.next
        prev = temp_current
    
        for _ in range(m,n):
            next = current.next
            current.next = prev
            prev = current
            current = next
        current.next = prev
        if start:
            start.next = current
        else:
            A = current
    
        return A
