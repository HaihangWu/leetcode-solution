class Solution {
public:
    void solveSudoku(vector < vector < char >> & board)
            {
                backtrack(board);
            }

private:
bool backtrack(vector < vector < char >> & board)
{
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            if (board[i][j] == '.') {
                for (char c = '1'; c <= '9'; ++c) {
                    if (isValid(board, i, j, c)) {
                        board[i][j] = c;
                        if (backtrack(board)) {
                            return true;
                        }
                        board[i][j] = '.';
                    }
                }
                return false;
            }
        }
    }
    return true;
}

bool isValid(vector < vector < char >> & board, int row, int col, char c) {
    for (int i = 0; i < 9; ++i) {
        if (board[row][i] == c)
            return false;
        }
        for (int i = 0; i < 9; ++i) {
            if (board[i][col] == c) return false;
        }
        int startRow = (row / 3) * 3;
        int startCol = (col / 3) * 3;
        for (int i = 0; i < 3; ++i)
        {
            for (int j = 0; j < 3; ++j) {
                if (board[startRow + i][startCol + j] == c)
                    return false;
            }
        }
        return true;
    }
};
