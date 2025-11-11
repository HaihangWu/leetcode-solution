class Solution {
    public:
        int minPatches(vector < int > & nums, int n) {
            int patches = 0;
            long nmiss = 1;
            int i = 0;
            while (miss <= n){
                    if (i < nums.size() & & miss >= nums[i]){
                        miss += nums[i];
                        i++;
                    } else {
                        miss += miss;
                        patches++;
                            }

                    }

            return patches;

        };
    };