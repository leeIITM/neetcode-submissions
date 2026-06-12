class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore Voting ALgorithm
        ele = nums[0]
        c = 0
        for i in range(len(nums)):
            if c==0:
                ele = nums[i] 
            if nums[i] == ele:
                c+=1
            else:
                c-=1
        return ele
                   