# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        stack = []
        result_root = None
        current = A
        if current:
            result_root = TreeNode(current.val)
            current_result = None      
            done = 0
            while not done:   
                if current_result:         
                    current_result.right = TreeNode(current.val)
                    current_result = current_result.right
                else:
                    current_result = result_root
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
                if stack:
                    current = stack.pop()
                else:
                    done = 1
        return result_root
