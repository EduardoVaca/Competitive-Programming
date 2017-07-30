# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invert_recursion(self, root):
        if root:
            aux = root.left
            root.left = root.right
            root.right = aux
            self.invert_recursion(root.left)
            self.invert_recursion(root.right)
            
    # @param root : root node of tree
    # @return the root node in the tree
    def invertTree(self, root):
        self.invert_recursion(root)
        return root
