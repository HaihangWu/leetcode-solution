class Solution {
public:
    std::vector<std::vector<std::string>> solveNQueens(int n) {
        std::vector<int> ans;
        std::vector<std::vector<std::string>> board;
        backtracking(ans, board, n);
        return board;
    }

private:
    void backtracking(std::vector<int>& answer, std::vector<std::vector<std::string>>& board, int n) {
        if (answer.size() == n) {
            std::vector<std::string> tempBoard;
            for (int i = 0; i < n; i++) {
                std::string row(n, '.');
                row[answer[i]] = 'Q';
                tempBoard.push_back(row);
            }
            board.push_back(tempBoard);
            return;
        }

        for (int i = 0; i < n; i++) {
            bool position = true;
            if (std::find(answer.begin(), answer.end(), i) != answer.end()) {
                position = false;
            }
            for (int index = 0; index < answer.size(); index++) {
                int ele = answer[index];
                if (std::abs(static_cast<int>(i - ele)) == std::abs(static_cast<int>(answer.size() - index))) {
                    position = false;
                }
            }
            if (position) {
                answer.push_back(i);
                backtracking(answer, board, n);
                answer.pop_back();
            }
        }
    }
};
