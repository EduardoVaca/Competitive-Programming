# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def getNodeFromArray(self, start, end, array):
        if start > end:
            return None
        mid = (start+end)/2        
        new_node = TreeNode(array[mid])
        new_node.left = self.getNodeFromArray(start, mid-1, array)
        new_node.right = self.getNodeFromArray(mid+1, end, array)
        return new_node
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.getNodeFromArray(0, len(nums)-1, nums)