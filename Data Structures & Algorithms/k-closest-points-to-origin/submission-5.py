class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max heap approach
        max_heap = []
        for i in points:
            heapq.heappush(max_heap,[-(i[0]**2 + i[1]**2), i])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        out = []
        while max_heap:
            out.append(heapq.heappop(max_heap)[1])
        return out