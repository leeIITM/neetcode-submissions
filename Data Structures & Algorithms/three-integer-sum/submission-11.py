class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < len(nums) and j < k:
                if nums[i] > 0:
                    break
                target = nums[i] + nums[j] + nums[k]
                if target > 0:
                    k -= 1
                elif target < 0:
                    j +=1
                else:
                    out.append([nums[i], nums[j], nums[k]])
                    j+=1
        o = [sorted(i) for i in out]
        p = []
        for j in o:
            if j not in p:
                p.append(j)
            else:
                pass
        return p