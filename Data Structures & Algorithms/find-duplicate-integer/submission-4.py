class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l+ r) // 2
            c = sum([1 for i in nums if i <= mid])
            if c <= mid :
                l = mid + 1
            else:
                r = mid 
        return l

        