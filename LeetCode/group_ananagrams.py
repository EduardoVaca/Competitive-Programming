class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        keys = dict()
        index = 0
        for word in strs:
            sort_word = ''.join(sorted(word))
            if sort_word in keys:
                result[keys[sort_word]].append(word)
            else:
                keys[sort_word] = index
                result.append([word])
                index += 1
        return result
        