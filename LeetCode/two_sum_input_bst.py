# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def findTargetUtil(self, root, k, val_set):
        if not root:
            return False
        if k-root.val in val_set:
            return True
        else:
            val_set.add(root.val)
        return self.findTargetUtil(root.left, k, val_set) or self.findTargetUtil(root.right, k, val_set)
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        return self.findTargetUtil(root, k, set())