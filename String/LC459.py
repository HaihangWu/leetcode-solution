class Solution(object):
    def build_lps(self, pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0
        for i in range(1, m, 1):
            while length > 0 and pattern[length] != pattern[i]:
                length = lps[length - 1]

            if pattern[length] == pattern[i]:
                length += 1
                lps[i] = length
        return lps

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        size = len(s)
        lps = self.build_lps(s)
        print(lps)
        overlap_size = lps[-1]
        repeated_size = size - lps[-1]
        if overlap_size == 0:
            return False
        elif overlap_size > 0 and overlap_size % repeated_size == 0:
            return True
        else:
            return False

