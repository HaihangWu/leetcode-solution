class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        digits = deque()
        n = len(tokens)
        tmp_result = None
        for i in range(n):
            if tokens[i] == '*' or tokens[i] == '/' or tokens[i] == '+' or tokens[i] == '-':
                tmp1 = digits.pop()
                tmp2 = digits.pop()
                if tokens[i] == '/':
                    tmp_result = int(float(tmp2) / tmp1)
                else:
                    tmp_result = int(ops[tokens[i]](tmp2, tmp1))
                digits.append(tmp_result)
            else:
                digits.append(int(tokens[i]))
        if tmp_result is None:
            if len(digits) > 0:
                return digits.pop()
        else:
            return tmp_result
