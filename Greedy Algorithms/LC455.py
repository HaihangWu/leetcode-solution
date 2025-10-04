class Solution(object):
    def solveSudoku(self, board):
        index_blank = []
        row_digits = [set() for _ in range(9)]
        col_digits = [set() for _ in range(9)]
        square_digits = [[set() for _ in range(3)] for _ in range(3)]

        # Initialize state
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    index_blank.append((i, j))
                else:
                    d = int(board[i][j])
                    row_digits[i].add(d)
                    col_digits[j].add(d)
                    square_digits[i//3][j//3].add(d)

        def backtracking():
            if not index_blank:
                return True  # solved

            # MRV heuristic: pick blank with fewest candidates
            index_blank.sort(key=lambda pos: len(
                {1,2,3,4,5,6,7,8,9} - (row_digits[pos[0]] | col_digits[pos[1]] | square_digits[pos[0]//3][pos[1]//3]))
            )
            i, j = index_blank.pop(0)

            for d in range(1, 10):
                if d not in row_digits[i] and d not in col_digits[j] and d not in square_digits[i//3][j//3]:
                    board[i][j] = str(d)
                    row_digits[i].add(d)
                    col_digits[j].add(d)
                    square_digits[i//3][j//3].add(d)

                    if backtracking():
                        return True

                    # undo
                    board[i][j] = '.'
                    row_digits[i].remove(d)
                    col_digits[j].remove(d)
                    square_digits[i//3][j//3].remove(d)

            index_blank.insert(0, (i, j))  # put back for other branches
            return False

        backtracking()
