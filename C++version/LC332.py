class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, priority_queue<string, vector<string>, greater<string>>> graph;
        for (const auto& ticket : tickets) {
            string src = ticket[0], dst = ticket[1];
            graph[src].push(dst);
        }
        vector<string> route;
        dfs("JFK", graph, route);
        return vector<string>(route.rbegin(), route.rend());  // Reverse the route to get correct order
    }

private:
    void dfs(const string& airport, unordered_map<string, priority_queue<string, vector<string>, greater<string>>>& graph, vector<string>& route) {
        auto& heap = graph[airport];
        while (!heap.empty()) {
            string next_airport = heap.top();
            heap.pop();
            dfs(next_airport, graph, route);
        }
        route.push_back(airport);
    }
};
