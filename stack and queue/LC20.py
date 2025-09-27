class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        n = len(s)
        left_bracket = deque()
        for i in range(n):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                left_bracket.append(s[i])
            elif s[i] == ')' or s[i] == ']' or s[i] == '}':
                if len(left_bracket) == 0:
                    return False
                tmp = left_bracket.pop()
                if (s[i] == ')' and tmp == '(') or (s[i] == ']' and tmp == '[') or (s[i] == '}' and tmp == '{'):
                    pass
                else:
                    return False
        if len(left_bracket) == 0:
            return True
        else:
            return False

