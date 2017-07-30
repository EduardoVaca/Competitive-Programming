# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        queue1 = []
        queue2 = []
        if root:
            queue1.append(root)
            while queue1 or queue2:
                if queue1:
                    while queue1:
                        current = queue1.pop(0)                    
                        current.next = queue1[0] if queue1 else None
                        if current.left:
                            queue2.append(current.left)
                        if current.right:
                            queue2.append(current.right)
                elif queue2:
                    while queue2:
                        current = queue2.pop(0)                    
                        current.next = queue2[0] if queue2 else None
                        if current.left:
                            queue1.append(current.left)
                        if current.right:
                            queue1.append(current.right)
        
