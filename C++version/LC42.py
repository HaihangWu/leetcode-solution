class Solution {
public:
    int trap(std::vector<int>& height) {
        std::deque<int> stack;
        int rain_amount = 0;
        for (int i = 0; i < height.size(); ++i) {
            int index = i;
            int ele = height[i];
            while (!stack.empty()) {
                if (ele > height[stack.back()]) {
                    int bottom = stack.back();
                    stack.pop_back();
                    int lowest = height[bottom];
                    if (stack.empty())
                        break;
                    rain_amount += (std::min(ele, height[stack.back()]) - lowest) * (index - stack.back() - 1);
                } else {
                    break;
                }
            }
            stack.push_back(index);
        }
        return rain_amount;
    }
};
