class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def countSubstrings(s):
            n = len(s)

        count = 0

        def expand(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(n):
            expand(i, i)  # 奇数长度回文
            expand(i, i + 1)  # 偶数长度回文

        return count



