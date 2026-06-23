class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Brute
        i = 0
        j = k
        max_ele = max(nums[i:j])
        #l = [max_ele]
        l = []
        for i in range(len(nums) - k+1):
            
            l.append(max(nums[i:j]))
            j+=1
        return l