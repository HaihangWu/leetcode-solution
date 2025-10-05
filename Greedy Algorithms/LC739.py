class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = list(str(n))
        mark = len(digits)

        # 从右向左遍历
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                mark = i  # 记录要变成 9 的起始位置

        # 将 mark 及其右边全部变成 '9'
        for i in range(mark, len(digits)):
            digits[i] = '9'

        return int("".join(digits))
