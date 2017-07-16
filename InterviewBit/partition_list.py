# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        current = A
        prev = current
        result = current_result = None
        
        # Get smaller
        while current:
            if current.val < B:
                # Add node to result
                if not result:
                    result = ListNode(current.val)
                    current_result = result
                else:
                    current_result.next = ListNode(current.val)
                    current_result = current_result.next
                # Delete smaller from original
                if current == A:
                    A = current.next
                else:
                    prev.next = current.next
            else:
                prev = current
            current = current.next
    
        # Add biggers
        if not result:
            result = A
        else:
            current_result.next = A
    
        return result
