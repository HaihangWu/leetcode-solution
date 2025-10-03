class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        size = len(s)
        res = []
        ans = []

        def isPalindrome(subs):
            return subs == subs[::-1]

        def backtracking(start):
            if start == size:
                res.append(ans[:])
                return

            for i in range(start + 1, size + 1):
                subs = s[start:i]
                if isPalindrome(subs):
                    ans.append(subs)
                    backtracking(i)
                    ans.pop()

        backtracking(0)

        return res

