class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def f(i,target,out : List[int]):
            
            if target == 0:
                return res.append(out.copy())
            elif i >=len(nums) or target < 0:
                return
                
            # pick
            out.append(nums[i])
            f(i,target - nums[i], out)

            # not pick
            out.pop()
            f(i+1, target , out)
        f(0,target,[])
        return res

        
        