class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # brute
        n = len(nums)
        d = []
        out = []
        for i in range(len(nums)):
            if nums[i] not in d:
                d.append(nums[i])
        for i in range(len(d)):
            if nums.count(d[i]) > n//3:
                out.append(d[i])
        return out


        