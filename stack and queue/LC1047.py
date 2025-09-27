class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        n = len(s)
        char_stack = deque()
        char_list = []
        for i in range(n):
            if len(char_stack) > 0 and char_stack[-1] == s[i]:
                char_stack.pop()
            else:
                char_stack.append(s[i])

        if len(char_stack) > 0:
            while len(char_stack):
                tmp = char_stack.pop()
                char_list.append(tmp)
            left = 0
            right = len(char_list) - 1
            while left < right:
                char_list[left], char_list[right] = char_list[right], char_list[left]
                left += 1
                right -= 1
            return ''.join(char_list)
        else:
            return ""