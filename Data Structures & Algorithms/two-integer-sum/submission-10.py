class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This is sorting based not hashmap
        hash = {}
        for i,j in enumerate(nums):
            hash[i] = j
        l = sorted(nums)
        p = 0
        q = len(l) - 1
        ret = []
        while p < q:
            if l[p] + l[q]> target:
                q-=1
            elif l[p] + l[q] < target:
                p+=1
            else:
                ret = [l[p], l[q]]
                break
        k1 = [k for k,v in hash.items() if v ==l[p]]
        del hash[k1[0]]
        k2 = [k for k,v in hash.items() if v ==l[q]]
        return sorted([k1[0],k2[0]])

