class Solution {
public:
    int largestRectangleArea(vector < int > & heights) {
            deque < int > stack;
            vector < int > answer(heights.size(), 0);
            heights.insert(heights.begin(), 0);
            heights.push_back(0);
            int max_area = 0;
            for (int i=0;i < heights.size();i + +){
                int index = i, height = heights[i];
                while (!stack.empty()){
                        if (height >= heights[stack.back()]){
                            break;
                            }
                        else {
                                int tmp = stack.back();
                                stack.pop_back();
                                answer[tmp - 1] = heights[tmp] * (index - stack.back() - 1);
                                max_area = max(max_area, heights[tmp] * (index - stack.back() - 1));
                                }
                        }
                stack.push_back(index);
        }
        return max_area;

    }
};