class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        mini =1
        for i in range(len(nums)):
            if nums[i] > 0:
                if nums[i] == mini:
                    mini +=1
                elif nums[i] < mini :
                    pass
                else:
                    return mini
        return max(nums) + 1 if max(nums) + 1 > 0 else 1

        