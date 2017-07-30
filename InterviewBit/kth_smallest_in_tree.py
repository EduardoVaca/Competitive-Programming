# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # @param root : root node of tree
    # @param k : integer
    # @return an integer
    def kthsmallest(self, root, k):
        stack = []
        small_index = 0
        current = root
        done = 0
        while not done:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                small_index += 1
                if small_index == k:
                    return current.val
                current = current.right
            else:
                done = 1
        return -1
                
                
        
