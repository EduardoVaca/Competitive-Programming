# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sum_to_leaf(self, root, current_sum):
        if not root.left and not root.right:
            return int(current_sum + str(root.val))
        elif root.left and root.right:
            return self.sum_to_leaf(root.left, current_sum+str(root.val)) + self.sum_to_leaf(root.right, current_sum+str(root.val))
        elif root.left:
            return self.sum_to_leaf(root.left, current_sum+str(root.val))
        else:
            return self.sum_to_leaf(root.right, current_sum+str(root.val))
    
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sum_to_leaf(root, '') if root else 0
        