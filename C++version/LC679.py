class Solution {
public:
    bool judgePoint24(vector<int>& cards) {
        vector<double> nums;
        for (int card : cards) {
            nums.push_back((double)card);
        }
        return backtrack(nums);
    }

private:
    bool backtrack(vector<double>& nums) {
        int n = nums.size();

        if (n == 1) {
            return fabs(nums[0] - 24.0) < 1e-6;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    vector<double> remaining;
                    for (int k = 0; k < n; k++) {
                        if (k != i && k != j) remaining.push_back(nums[k]);
                    }

                    vector<double> results = {
                        nums[i] + nums[j], // 加法
                        nums[i] - nums[j], // 减法
                        nums[i] * nums[j], // 乘法
                    };

                    if (nums[j] != 0) {
                        results.push_back(nums[i] / nums[j]);
                    }

                    for (double res : results) {
                        remaining.push_back(res);
                        if (backtrack(remaining)) return true;
                        remaining.pop_back();
                    }
                }
            }
        }
        return false;
    }
};