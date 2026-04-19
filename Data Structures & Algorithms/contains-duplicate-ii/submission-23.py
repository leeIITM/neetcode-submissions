class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        import math
        for i in range(len(nums)):
            if nums[i] in d:
                if math.fabs(i - d[nums[i]]) <=k:
                    return True
                else:
                    d[nums[i]] = i
            else:
                d[nums[i]] = i
        return False
