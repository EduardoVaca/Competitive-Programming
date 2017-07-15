# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def sum_nodes(A, B, extra):
    if A and B:
        return (A.val+B.val+extra if A.val+B.val+extra  < 10 else (A.val+B.val+extra )%10, 0 if A.val+B.val+extra  < 10 else 1)
    elif A:
        return (A.val+extra if A.val+extra < 10 else (A.val+extra )%10, 0 if A.val+extra < 10 else 1)
    elif B:
        return (B.val+extra if B.val+extra < 10 else (B.val+extra)%10, 0 if B.val+extra < 10 else 1)
    else:
        return (-1,-1)

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        if A or B:
            current_A = A
            current_B = B
            sum_res = sum_nodes(current_A, current_B, 0)
            result = ListNode(sum_res[0])
            trailing = sum_res[1]
            current_result = result
            current_A = current_A.next if current_A else None
            current_B = current_B.next if current_B else None
            last_valid_node = current_result if current_result.val > 0 else None
            while current_A or current_B:
                sum_res = sum_nodes(current_A, current_B, trailing)
                trailing = sum_res[1]
                current_result.next = ListNode(sum_res[0])
                current_A = current_A.next if current_A else None
                current_B = current_B.next if current_B else None
                current_result = current_result.next
                last_valid_node = current_result if current_result.val > 0 else None
            if trailing > 0:
                current_result.next = ListNode(trailing)
            else:
                last_valid_node.next = None
            return result
        else:
            return None
