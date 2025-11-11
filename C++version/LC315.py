class Solution {
public: vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> counts(n, 0);
        vector<int> indices(n, 0);
        for (int i = 0; i < n; ++i) indices[i] = i;
        mergeSort(nums, indices, 0, n - 1, counts);
        return counts;
    }

private:
    void mergeSort(vector<int>& nums, vector<int>& indices, int left, int right, vector<int>& counts) {
        if (left >= right) return;
        int mid = (left + right) / 2;
        mergeSort(nums, indices, left, mid, counts);
        mergeSort(nums, indices, mid + 1, right, counts);
        merge(nums, indices, left, mid, right, counts);
    }

    void merge(vector<int>& nums, vector<int>& indices, int left, int mid, int right, vector<int>& counts) {
        vector<int> temp(right - left + 1);
        int i = left, j = mid + 1, k = 0;
        int rightCount = 0;

        while (i <= mid && j <= right) {
            if (nums[indices[j]] < nums[indices[i]]) {
                rightCount++;
                temp[k++] = indices[j++];
            } else {
                counts[indices[i]] += rightCount;
                temp[k++] = indices[i++];
            }
        }

        while (i <= mid) {
            counts[indices[i]] += rightCount;
            temp[k++] = indices[i++];
        }
        while (j <= right) {
            temp[k++] = indices[j++];
        }

        for (int t = 0; t < temp.size(); ++t) {
            indices[left + t] = temp[t];
        }
    }
};