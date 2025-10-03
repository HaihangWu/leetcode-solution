class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        digits = list(digits)
        size = len(digits)
        if size == 0:
            return []

        digits = [list(phone_map[digit]) for digit in digits]
        answer = []
        res = []

        def backtracking(depth):
            if depth == size:
                res.append(''.join(answer[:]))
                return

            for index, ele in enumerate(digits[depth]):
                answer.append(ele)
                backtracking(depth + 1)
                answer.pop()

        backtracking(0)

        return res



