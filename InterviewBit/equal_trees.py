# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:

    def is_equal_tree(self, A, B):
        if not A and not B:
            return True
        elif A and B:
            return A.val == B.val and self.is_equal_tree(A.left, B.left) and self.is_equal_tree(A.right, B.right)
        else:
            return False

    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        return 1 if self.is_equal_tree(A, B) else 0