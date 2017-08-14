# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        first = True
        swap = True
        current = head
        prev = current
        while current.next:
            if swap:
                temp = current.next
                current.next = current.next.next
                temp.next = current
                if first:
                    head = temp
                    first = False
                else:
                    prev.next = temp
                    prev = current
                swap = False
            else:
                current = current.next if current.next else current
                swap = True
        return head
                
                    