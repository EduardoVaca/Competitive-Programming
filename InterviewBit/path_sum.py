# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    
    def is_leaf(self, root):
        return root.right == None and root.left == None
    
    def path_sum_exists(self, root, current_sum, total_sum):
        if not root:
            return False
        current_sum += root.val
        if current_sum == total_sum and self.is_leaf(root):
            return True
        else:
            return self.path_sum_exists(root.left, current_sum, total_sum) or \
                    self.path_sum_exists(root.right, current_sum, total_sum)
    
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        return 1 if self.path_sum_exists(A, 0, B) else 0