class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        char_b = [None] * 26
        size = len(s)
        for i in range(26):
            for j in range(size - 1, -1, -1):
                if ord(s[j]) - ord('a') == i:
                    char_b[i] = j
                    break
        boundary = 0
        farest = 0
        sol = []
        for i, c in enumerate(s):
            index = ord(c) - ord('a')
            farest = max(farest, char_b[index])
            if i == farest:
                sol.append(i + 1 - boundary)
                boundary = i + 1
                farest = char_b[index]
        return sol






