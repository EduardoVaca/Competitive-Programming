class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        current_missing = 1
        for n in nums:
            if n == current_missing:
                seen.add(n)
                while current_missing in seen:
                    current_missing += 1
            elif n > 0:
                seen.add(n)
        return current_missing
        