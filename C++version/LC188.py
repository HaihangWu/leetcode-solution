class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n=prices.size();
        if (k >= n/2){
            int total=0;
            for (int i=0;i<n-1;i++){
                total+=std::max(prices[i+1]-prices[i],0);
            }
            return total;
        }
        vector<vector<int>> dp(k+1,vector<int>(2,0));
        for(int j=0;j<k+1;j++){
            dp[j][1] = INT_MIN;
        }
        for (int price:prices){
            for(int j=k;j>0;j--){
                dp[j][0] = max(dp[j][0], dp[j][1] + price);
                dp[j][1] = max(dp[j][1], dp[j-1][0] - price);
            }
        }
        return dp[k][0];
    }
};
