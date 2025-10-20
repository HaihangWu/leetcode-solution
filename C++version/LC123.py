
class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        if (prices.empty()) {
            return 0;
        }
        int dp0 = 0;
        int dp1 = -prices[0];
        int dp2 = 0;
        int dp3 = -prices[0];
        int dp4 = 0;
        for (int p : prices) {
            dp1 = std::max(dp1, dp0 - p);
            dp2 = std::max(dp2, dp1 + p);
            dp3 = std::max(dp3, dp2 - p);
            dp4 = std::max(dp4, dp3 + p);
        }
        return dp4;
    }
};
