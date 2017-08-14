class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        subsets_set = set()
        for num in sorted(nums):
            current_result = []
            for item in result:
                current_subset = item+[num]
                key = ','.join(str(x) for x in current_subset)
                if key not in subsets_set:
                    current_result += [current_subset]
                    subsets_set.add(key)                     
            result += current_result
        return result
        