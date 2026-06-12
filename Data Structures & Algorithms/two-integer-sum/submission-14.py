class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''This is Hashmap based but its cleverer bcoz even though 
        you dont store all indices but you store the later indices and search 
        from lower indices '''
        # Now lets do single pass
        
        hash = {}
        for i, val in enumerate(nums):
            diff = target - nums[i]
            if diff in hash and hash[diff] !=i:
                return sorted([i,hash[diff]])
            else:
                pass
            hash[val] = i