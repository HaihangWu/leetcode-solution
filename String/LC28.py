class Solution(object):
    def build_lps(self, pattern):
        n = len(pattern)
        lps = [0] * n
        length = 0
        i = 1
        while i < n:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length == 0:
                    lps[i] = 0
                    i += 1
                else:
                    length = lps[length - 1]
        return lps

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        needle = list(needle)
        haystack = list(haystack)
        n = len(haystack)
        m = len(needle)
        lps = self.build_lps(needle)
        length = 0

        for i in range(n):
            while length > 0 and haystack[i] != needle[length]:
                length = lps[length - 1]  # 利用 LPS 回退模式串指针

            if haystack[i] == needle[length]:
                length += 1

            if length == m:
                return i - m + 1  # 找到匹配

        return -1



