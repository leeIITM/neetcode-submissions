class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [[(i[0]**2 + i[1]**2)**0.5 ,i] for i in points]

        import heapq
        heapq.heapify(dist)
        out = []
        for i in range(k):
            p = heapq.heappop(dist)
            out.append(p[1])
        return out