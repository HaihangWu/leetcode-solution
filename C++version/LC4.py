class Solution {
        public:int partition(std::vector < int > & arr, int low, int high) {
                int pivot = arr[high];
                int i = low - 1;
                for (int j = low; j < high; ++j)
                {
                    if (arr[j] <= pivot)
                        {
                            ++i;
                            std::swap(arr[i], arr[j]);
                        }
                }
                std::swap(arr[i + 1], arr[high]);
                return i + 1;
            }

        void quicksort(std::vector < int > & arr, int low, int high) {
                if (low < high)
                {
                    int pi = partition(arr, low, high);
                    quicksort(arr, low, pi - 1);
                    quicksort(arr, pi + 1, high);
                }
            }

        double findMedianSortedArrays(vector < int > & nums1, vector < int > & nums2) {
                vector < int > all_num = nums1;
                all_num.insert(all_num.end(), nums2.begin(), nums2.end());
                quicksort(all_num, 0, all_num.size() - 1);
                int mid_index = (all_num.size()) / 2;
                if ((all_num.size()) % 2 == 0){
                    return (all_num[mid_index] + all_num[mid_index - 1]) / 2.0;
                }
                else {
                    return all_num[mid_index];
                }
            }
};