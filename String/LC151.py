class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        n = len(s)
        slow = 0
        fast = 0
        word_start = False
        word_size = 0
        while fast < n:
            if s[fast] != " ":
                if slow == 0:
                    pass
                else:
                    s[slow] = " "
                    slow += 1
                while fast < n and s[fast] != " ":
                    s[slow] = s[fast]
                    slow += 1
                    fast += 1
            fast += 1

        s = s[0:slow]
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        word_left = 0
        word_right = 0
        for i in range(n):
            if s[i] == " " or i == n - 1:
                word_right = i if i == n - 1 else i - 1
                while word_left < word_right:
                    s[word_left], s[word_right] = s[word_right], s[word_left]
                    word_left += 1
                    word_right -= 1
                word_left = i + 1
        return "".join(s)
