class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = nums.count(nums[i])
            else:
                pass
        ret = [[d[i],i] for i in d]
        ret_s = sorted(ret,reverse = True)
        return [ret_s[i][1] for i in range(k)]