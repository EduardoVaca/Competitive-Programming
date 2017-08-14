# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        current_result = None
        trailing = 0
        current_l1 = l1
        current_l2 = l2
        while current_l1 or current_l2:
            if current_l1 and current_l2:
                current_sum = current_l1.val + current_l2.val + trailing 
            elif current_l1:
                current_sum = current_l1.val + trailing
            else:
                current_sum = current_l2.val + trailing
            trailing = 0 if current_sum < 10 else 1
            current_sum = current_sum if trailing == 0 else current_sum - 10
            if current_result:
                current_result.next = ListNode(current_sum)
                current_result = current_result.next
            else:
                result = ListNode(current_sum)
                current_result = result
            current_l1 = current_l1.next if current_l1 else None
            current_l2 = current_l2.next if current_l2 else None
        if trailing == 1:
            current_result.next = ListNode(1)
        return result
        