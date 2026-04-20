class Solution:
    def rob(self, nums: List[int]) -> int:
        # If i pick the first element
        nums1 = nums[2:-1] # need to add first element

        # If i dont pick the first element\
        nums2 = nums[1 : ]
        def max_rob(nums1):
            rob1, rob2 = 0 ,0
            for num in nums1:
                temp = max(num + rob1 , rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        elem1 = nums[0] + max_rob(nums1)
        elem2 = max_rob(nums2)
        return max(elem1,elem2)