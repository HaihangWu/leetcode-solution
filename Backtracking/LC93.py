class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        size = len(s)
        res = []
        ans = []

        def isvalid(sub):
            if sub[0] == "0":
                if len(sub) >= 2:
                    return False
                else:
                    return True
            else:
                if int(sub) >= 256 or int(sub) < 0:
                    return False
                else:
                    return True

        def backtracking(start):
            if len(ans) == 4:
                if start == size:
                    res.append(".".join(ans))
                return

            for i in range(start + 1, size + 1):
                subs = s[start:i]
                if isvalid(subs):
                    ans.append(subs)
                    backtracking(i)
                    ans.pop()

        backtracking(0)
        return res


