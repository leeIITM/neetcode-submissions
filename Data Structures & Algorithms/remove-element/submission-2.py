class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 2**16 - 1
            else:
                c+=1
            
        nums.sort()
        return c
