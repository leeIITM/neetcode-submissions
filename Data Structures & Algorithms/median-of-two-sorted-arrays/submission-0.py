class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Brute O(m + n)
        output = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i]  <  nums2[j]:
                output.append(nums1[i])
                i += 1
            else:
                output.append(nums2[j])
                j+=1
        while i < len(nums1):
            # print("ff")
            output = output + nums1[i :]
            break
        while j < len(nums2):
            # print("its happening")
            output = output + nums2[j :]
            break
        n = len(nums1) 
        m = len(nums2)
        print(output)
        if (n + m) % 2 == 0:
            i = (n + m) // 2
            median = (output[i -1] + output[i]) /2
            print(median)
        else:
            i = (n + m) //2
            median = output[i]
        return float(median)

            