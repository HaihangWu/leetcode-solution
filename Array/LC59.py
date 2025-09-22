class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[None for _ in range(n)] for _ in range(n)]
        start_row = 0
        start_col = 0
        offset = 0
        count = 0
        loop = n // 2
        while loop > 0:
            row_index = start_row
            col_index = start_col
            for col_index in range(start_col, n - offset - 1, 1):
                count += 1
                matrix[row_index][col_index] = count
            for row_index in range(start_row, n - offset - 1, 1):
                count += 1
                matrix[row_index][col_index + 1] = count
            for col_index in range(n - offset - 1, offset, -1):
                count += 1
                matrix[row_index + 1][col_index] = count
            for row_index in range(n - offset - 1, offset, -1):
                count += 1
                matrix[row_index][col_index - 1] = count
            loop -= 1
            offset += 1
            start_row += 1
            start_col += 1

        if n % 2 != 0:
            count += 1
            row_index = n // 2
            col_index = n // 2
            matrix[row_index][col_index] = count

        return matrix