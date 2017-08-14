# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current = head
        eliminate = current
        prev = current
        wait = 1
        while current.next:
            if wait >= n:
                eliminate = eliminate.next
            if wait >= n+1:
                prev = prev.next
            wait += 1
            current = current.next
            
        if eliminate == head:
            head = head.next
        else:
            prev.next = eliminate.next
        return head