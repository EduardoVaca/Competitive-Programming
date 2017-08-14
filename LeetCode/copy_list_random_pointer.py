# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        new_head, new_current, current, nodes_dict = None, None, head, dict()
        while current:
            if not new_head:
                new_head = RandomListNode(current.label)
                new_current = new_head                                       
            if current.next:
                if current.next.label in nodes_dict:
                    new_current.next = nodes_dict[current.next.label]
                else:
                    new_current.next = RandomListNode(current.next.label)
                    nodes_dict[new_current.next.label] = new_current.next
            if current.random:
                if current.random.label in nodes_dict:
                    new_current.random = nodes_dict[current.random.label]
                else:
                    new_current.random = RandomListNode(current.random.label)
                    nodes_dict[new_current.random.label] = new_current.random
            if new_current.label not in nodes_dict:
                nodes_dict[new_current.label] = new_current
            new_current = new_current.next
            current = current.next
        return new_head
        
        