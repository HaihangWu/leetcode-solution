from collections import defaultdict
import heapq


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        # Build min-heap adjacency list for lexicographical order
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        route = []

        def dfs(airport):
            heap = graph[airport]
            while heap:
                next_airport = heapq.heappop(heap)
                dfs(next_airport)
            route.append(airport)  # post-order

        dfs("JFK")
        return route[::-1]  # reverse to get correct order
