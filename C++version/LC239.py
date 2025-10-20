class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int size_n=nums.size();
        if (size_n==0 or k==0){return {};}
        deque<int> q;
        vector<int> res;
        for (int i=0;i<size_n;i++){
            if (!q.empty() and q.front() <i-k+1)
                q.pop_front();
            while (!q.empty()  and nums[q.back()]<nums[i])
                q.pop_back();
            q.push_back(i);
            if (i>=k-1)
                res.push_back(nums[q.front() ]);
        }
        return res;
    }
};