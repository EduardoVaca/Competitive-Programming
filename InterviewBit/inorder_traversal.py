# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        stack = []
        result = []
        current = A
        if current:
            stack.append(current)
            current = current.left
            while stack:            
                if current:
                    stack.append(current)
                    current = current.left
                else:
                    popped = stack.pop()
                    result.append(popped.val)
                    current = popped.right
                    if current:
                        stack.append(current)
                        current = current.left              
        return result