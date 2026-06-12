class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Three pointers without extra space I
        nums1_copy = nums1.copy()
        i,j = m -1 , n - 1
        k = m + n - 1
        while k >=0:
            if i < 0:
                nums1[k] = nums2[j]
                k,j = k-1,j-1
            elif j < 0:
                nums1[k] = nums1[i]
                k,i = k-1 , i-1
            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k,i = k-1,i-1
            elif nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                k,j = k-1,j-1
            else:
                nums1[k] = nums1[i]
                k,i = k-1,i -1
                    
