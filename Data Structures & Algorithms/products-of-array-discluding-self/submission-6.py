class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) == 1:
            print("dd")
            prod = 1
            for i,num in enumerate(nums):
                if num == 0:
                    rem  = i
                    pass
                else:
                    prod *= num
            print(prod)
            out = [0 for i in range(len(nums))]
            out[rem] = prod
            return out

        
        else:
            prod = 1
            for num in nums:
                prod *=num
            out = [prod for i in range(len(nums))]
            for i in range(len(nums)):
                if nums[i] == 0 :
                    pass
                else:
                    out[i] = int(out[i] / nums[i])
            return out
            
            