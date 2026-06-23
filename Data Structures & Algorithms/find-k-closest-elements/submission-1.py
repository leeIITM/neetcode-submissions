class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # This is O(n)
        if x < min(arr):
            l = arr[ : k]
        elif x > max(arr):
            l = arr[len(arr)-k : ]
        else:
            for i in range(0,len(arr)-1):
                
                if arr[i] <= x and arr[i+1] >=x:
                    index = i
                
            #print(index)
            i = index
            j = index + 1
            l = []
            while k > 0:
                if math.fabs(x - arr[i]) <= math.fabs(x - arr[j]):
                    l.append(arr[i])
                    i -= 1
                    k -= 1
                else:
                    l.append(arr[j])
                    j = j + 1
                    k-=1
            l = sorted(l)
        return l