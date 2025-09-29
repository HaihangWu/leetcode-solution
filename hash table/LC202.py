class Solution(object):
    def get_sum(self, n):
        result = 0
        while n:
            result += (n % 10) * (n % 10)
            n = n // 10
        return result

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        answer = n
        results = set()
        while True:
            answer = self.get_sum(answer)
            if answer == 1:
                return True
            if answer in results:
                return False
            else:
                results.add(answer)

