class Solution(object):
    
    def containsPattern(self, s, pattern):
        size_pattern = len(pattern)
        if len(s)%size_pattern != 0:
            return False
        else:
            for i in range(0, len(s), size_pattern):
                if s[i:i+size_pattern] != pattern:
                    return False
            return True
    
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(0, (len(s)/2)+1):
            if i > 0 and s[i] == s[0] and self.containsPattern(s, s[:i]):
                return True
        return False
        