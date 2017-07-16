# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        visited = set()
        current = A
        while current:
            if current.val in visited:
                return current
            else:
                visited.add(current.val)
                current = current.next
        return current
