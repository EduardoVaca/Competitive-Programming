# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue1 = []
        queue2 = []
        result = []
        if root:
            queue1.append(root)
        while queue1 or queue2:
            if queue1:
                result.append(queue1[-1].val)
                while queue1:
                    current = queue1.pop(0)
                    if current.left:
                        queue2.append(current.left)
                    if current.right:
                        queue2.append(current.right)
            elif queue2:
                result.append(queue2[-1].val)
                while queue2:
                    current = queue2.pop(0)
                    if current.left:
                        queue1.append(current.left)
                    if current.right:
                        queue1.append(current.right)
        return result
                
                