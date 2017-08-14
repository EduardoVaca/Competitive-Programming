class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_set = set()
        extra = None
        for num in nums:
            if num in nums_set:
                extra = num
                break
            else:
                nums_set.add(num)
        n = len(nums)
        correct_sum = n*(n+1)/2
        return [extra, extra+(correct_sum-sum(nums))]