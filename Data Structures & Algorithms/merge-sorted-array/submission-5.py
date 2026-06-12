class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Three pointers with extra space
        nums1_copy = nums1.copy()
        i,j,k = 0,0,0
        while k < m+n:
            if i >=m:
                nums1[k] = nums2[j]
                k,j = k+1,j+1
            elif j >=n:
                nums1[k] = nums1_copy[i]
                k,i = k+1 , i+1
            elif nums1_copy[i] > nums2[j]:
                nums1[k] = nums2[j]
                k , j = k+1,j+1
            elif nums1_copy[i] < nums2[j]:
                nums1[k] = nums1_copy[i]
                k,i = k+1,i+1
            else:
                nums1[k] = nums1_copy[i]
                k,i = k+1,i+1
                    
