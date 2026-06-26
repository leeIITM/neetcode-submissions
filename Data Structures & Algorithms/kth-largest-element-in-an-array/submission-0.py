class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        #print(minheap)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
        