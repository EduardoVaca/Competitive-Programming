# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """        
        nodes_A = set()
        currentA = headA
        while currentA:
            nodes_A.add(currentA.val)
            currentA = currentA.next
        currentB = headB
        while currentB:
            if currentB.val in nodes_A:
                return currentB
            currentB = currentB.next
        return None
        