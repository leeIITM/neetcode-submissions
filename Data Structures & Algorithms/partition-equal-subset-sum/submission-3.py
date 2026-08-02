class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 0:

            hash_map = {}

            def f(ind,summ1, summ2):
                if ind == len(nums):
                    if summ1  == summ2:
                        return True
                    else:
                        return False
                # Put in summ1
                if (ind  + 1, summ1 + nums[ind] , summ2) in hash_map:
                    one = hash_map[(ind + 1 , summ1 + nums[ind] , summ2)]
                else:

                    one = f(ind + 1 ,summ1 + nums[ind], summ2)
                    hash_map[(ind + 1 ,summ1 + nums[ind], summ2)] = one

                # Put in Summ2
                if (ind + 1 , summ1 , summ2 + nums[ind]) in hash_map:
                    two = f(ind + 1 , summ1 , summ2 + nums[ind])
                else:
                    two = f(ind + 1 , summ1 , summ2 + nums[ind])
                    hash_map[(ind + 1 , summ1 , summ2 + nums[ind])] = two
                    
                return one or two
            out = f(0,0,0)
            return out
        else:
            return False